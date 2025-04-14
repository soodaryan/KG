import asyncio
from datetime import datetime
from hashlib import md5
from langchain_text_splitters import TokenTextSplitter
from baseModels import Extraction
from prompts import import_query, graph_query, construction_prompt
from config import GOOGLE_API_KEY

from langchain_google_genai import ChatGoogleGenerativeAI

def encode_md5(text): return md5(text.encode("utf-8")).hexdigest()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key =  GOOGLE_API_KEY
)

structured_llm = llm.with_structured_output(Extraction)
construction_chain = construction_prompt | structured_llm

async def process_document(text, document_name, graph, chunk_size=2000, chunk_overlap=200):
    start = datetime.now()
    print(f"Started at: {start}")

    text_splitter = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_text(text)
    print(f"Chunks: {len(texts)}")

    tasks = [construction_chain.ainvoke({"input": t}) for t in texts]
    results = await asyncio.gather(*tasks)

    docs = [r.model_dump() for r in results]
    for i, doc in enumerate(docs):
        doc.update({
            "chunk_id": encode_md5(texts[i]),
            "chunk_text": texts[i],
            "index": i
        })
        for af in doc["atomic_facts"]:
            af["id"] = encode_md5(af["atomic_fact"])

    graph.query(import_query, params={"data": docs, "document_name": document_name})
    graph.query(graph_query, params={"document_name": document_name})

    print(f"Finished in: {datetime.now() - start}")

import asyncio
from config import NEO4J_URI_1, NEO4J_USERNAME_1, NEO4J_PASSWORD_1
from graph_utils import initialize_graph, clear_graph
from document_processor import process_document

if __name__ == "__main__":
    with open("data/sample_data.txt", "r", encoding="utf-8") as file:
        text = file.read()

    graph = initialize_graph(NEO4J_URI_1, NEO4J_USERNAME_1, NEO4J_PASSWORD_1)
    asyncio.run(process_document(text, "French revolution", graph, chunk_size=500, chunk_overlap=100))
    
    # to clear graph for new iteration 
    clear_graph(graph)

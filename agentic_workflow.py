import asyncio

from document_processor import process_document
from graph_utils import initialize_graph, clear_graph

def build_two_knowledge_graphs(clear = False):
    from config import NEO4J_URI_1, NEO4J_USERNAME_1, NEO4J_PASSWORD_1, NEO4J_URI_2, NEO4J_USERNAME_2, NEO4J_PASSWORD_2

    # Load docs
    with open("data/frameworks.txt", "r", encoding="utf-8") as f1:
        frameworks_text = f1.read()

    with open("data/secret_manual.txt", "r", encoding="utf-8") as f2:
        secret_manual_text = f2.read()

    # Init Graphs
    graph_A = initialize_graph(
        NEO4J_URI_1,
        NEO4J_USERNAME_1,
        NEO4J_PASSWORD_1
    )

    graph_B = initialize_graph(
        NEO4J_URI_2,
        NEO4J_USERNAME_2,
        NEO4J_PASSWORD_2
    )
    
    if clear :
        # Clear Graphs
        clear_graph(graph_A)
        clear_graph(graph_B)
    
    # Process Documents
    async def process_sequentially():
        print("Processing Frameworks...")
        await process_document(frameworks_text, "Frameworks", graph_A)
        print("Frameworks KG populated\n")

        print("Processing Secret Manual...")
        await process_document(secret_manual_text, "SecretManual", graph_B)
        print("Secret Manual KG populated")

    asyncio.run(process_sequentially())

    return graph_A, graph_B


def main() :
    # just for testing 
    
    A, B = build_two_knowledge_graphs(True)
    print("Executed Successfully")
    
main()
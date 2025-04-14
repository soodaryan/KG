from langchain_neo4j import Neo4jGraph
from prompts import clear_query

def initialize_graph(url, username, password):
    graph = Neo4jGraph(url=url, username=username, password=password, refresh_schema=False)

    constraints = [
        "CREATE CONSTRAINT IF NOT EXISTS FOR (c:Chunk) REQUIRE c.id IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (c:AtomicFact) REQUIRE c.id IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (c:KeyElement) REQUIRE c.id IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (d:Document) REQUIRE d.id IS UNIQUE"
    ]

    for constraint in constraints:
        graph.query(constraint)

    return graph

def clear_graph(graph):
    graph.query(clear_query)

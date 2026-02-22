import os
from dotenv import load_dotenv
from neo4j import GraphDatabase, basic_auth, Result

load_dotenv()

driver = GraphDatabase.driver(
  os.environ["NEO4J_URI"],
  auth=basic_auth(os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"]))


movie = "Toy Story"

## Graph

records, summary, keys = driver.execute_query("""
MATCH path = (person:Person)-[actedIn:ACTED_IN]->(movie:Movie {title: $title})
RETURN path, person, actedIn, movie
""", title=movie)

# print("records", records)
# print("summary", summary)
# print("keys", keys)

## Records

# for record in records:
#     node = record["movie"]
#     print(node.element_id)  # (1)
#     print(node.labels)  # (2)
#     print(node.items())  # (3)
#     print(node["name"])
#     print(node.get("name", "N/A"))

## Relationships
# for record in records:
#     acted_in = record["actedIn"]
#     print(acted_in.id)         # (1)
#     print(acted_in.type)       # (2)
#     print(acted_in.items())    # (3)
#     # 4
#     print(acted_in["roles"])
#     print(acted_in.get("roles", "(Unknown)"))
#     print(acted_in.start_node) # (5)
#     print(acted_in.end_node)   # (6)

## Paths
for record in records:
    path = record["path"]
    print(path.start_node)  # (1)
    print(path.end_node)  # (2)
    print(len(path))  # (1)
    print(path.relationships)  # (1)
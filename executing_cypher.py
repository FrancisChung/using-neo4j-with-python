from neo4j import GraphDatabase
driver = GraphDatabase.driver(
    "neo4j://localhost:7687",
    auth=("neo4j", "neo4jd0m3")
)
driver.verify_connectivity()
print("Driver connected")

cypher = """
MATCH (p:Person {name: $name})-[r:ACTED_IN]->(m:Movie)
RETURN m.title AS title, r.role AS role
"""

name = "Tom Hanks"

records, summary, keys = driver.execute_query(
    cypher,
    name=name
)

print(records)


driver.close()
print("Driver closed")
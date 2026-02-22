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

result = driver.execute_query(
    cypher,
    name=name,
    result_transformer_= lambda result: [
        f"Tom Hanks played {record['role']} in {record['title']}"
        for record in result
    ]
)
print(result)


driver.close()
print("Driver closed")
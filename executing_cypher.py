import os
from dotenv import load_dotenv
from neo4j import GraphDatabase, basic_auth, Result

load_dotenv()

driver = GraphDatabase.driver(
  os.environ["NEO4J_URI"],
  auth=basic_auth(os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"]))

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
print("result", result)


driver.close()
print("Driver closed")
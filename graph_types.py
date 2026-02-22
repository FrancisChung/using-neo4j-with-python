import os
from dotenv import load_dotenv
from neo4j import GraphDatabase, basic_auth, Result

load_dotenv()

driver = GraphDatabase.driver(
  os.environ["NEO4J_URI"],
  auth=basic_auth(os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"]))


movie = "Toy Story"

records, summary, keys = driver.execute_query("""
MATCH path = (person:Person)-[actedIn:ACTED_IN]->(movie:Movie {title: $title})
RETURN path, person, actedIn, movie
""", title=movie)

print("records", records)
print("summary", summary)
print("keys", keys)
from neo4j import GraphDatabase
driver = GraphDatabase.driver(
    "neo4j://localhost:7687",
    auth=("neo4j", "neo4jd0m3")
)
driver.verify_connectivity()
print("Driver connected")


records, summary, keys = driver.execute_query( # (1)
    "RETURN COUNT {()} AS count"
)
# Get the first record
first = records[0]      # (2)
# Print the count entry
print(first["count"])   # (3)

driver.close()
print("Driver closed")
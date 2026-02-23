import os
from dotenv import load_dotenv
from neo4j import GraphDatabase, basic_auth, Result
from neo4j.spatial import CartesianPoint


load_dotenv()

driver = GraphDatabase.driver(
  os.environ["NEO4J_URI"],
  auth=basic_auth(os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"]))


records, summary, keys = driver.execute_query("""
RETURN point({x: 1.23, y: 4.56, z: 7.89}) AS threeD
""")

point = records[0]["threeD"]

# <1> Accessing attributes
print(point.x, point.y, point.z, point.srid) # 1.23, 4.56, 7.89, 9157

# <2> Destructuring
x, y, z = point


from neo4j.spatial import WGS84Point

ldn = WGS84Point((-0.118092, 51.509865))
print(ldn.longitude, ldn.latitude, ldn.srid) # -0.118092, 51.509865, 4326

shard = WGS84Point((-0.086500, 51.504501, 310))
print(shard.longitude, shard.latitude, shard.height, shard.srid) # -0.0865, 51.504501, 310, 4979

# Using destructuring
longitude, latitude, height = shard


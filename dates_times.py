import os
from dotenv import load_dotenv
from neo4j import GraphDatabase, basic_auth, Result
from neo4j.time import DateTime, Duration
from datetime import timezone, timedelta


load_dotenv()

driver = GraphDatabase.driver(
  os.environ["NEO4J_URI"],
  auth=basic_auth(os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"]))


result = driver.execute_query("""
CREATE (e:Event {
  startsAt: $datetime,              // (1)
  createdAt: datetime($dtstring),   // (2)
  updatedAt: datetime()             // (3)
})
""",
    datetime=DateTime(
        2024, 5, 15, 14, 30, 0,
        tzinfo=timezone(timedelta(hours=2))
    ),  # (4)
    dtstring="2024-05-15T14:30:00+02:00"
)

print("Writing Result: ", result)

records, summary, keys = driver.execute_query("""
RETURN date() as date, time() as time, datetime() as datetime, toString(datetime()) as asString
""")

# Access the first record
for record in records:
    # Automatic conversion to Python driver types
    date = record["date"]           # neo4j.time.Date
    time = record["time"]           # neo4j.time.Time
    datetime = record["datetime"]   # neo4j.time.DateTime
    as_string = record["asString"]  # str

    print("Record:", date,"|",time, "|",datetime,"|",as_string)

starts_at = DateTime.now()
event_length = Duration(hours=1, minutes=30)
ends_at = starts_at + event_length
driver.execute_query("""
CREATE (e:Event {
  startsAt: $startsAt, endsAt: $endsAt,
  duration: $eventLength, // (1)
  interval: duration('P30M') // (2)
})
""",
    startsAt=starts_at, endsAt=ends_at, eventLength=event_length
)
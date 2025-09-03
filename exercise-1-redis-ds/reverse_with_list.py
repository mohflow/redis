#!/usr/bin/env python3
import redis
import json

with open("/home/coder/redis/exercise-1-redis-ds/config.json", "r") as f:
    config = json.load(f)

SOURCE_HOST = config["source_db"]
SOURCE_PORT = config["source_port"]
REPLICA_HOST = config["replica_db"]
REPLICA_PORT = config["replica_port"]


# Connect to source Redis
source_r = redis.Redis(host=SOURCE_HOST, port=SOURCE_PORT, decode_responses=True)
# Connect to replica Redis
replica_r = redis.Redis(host=REPLICA_HOST, port=REPLICA_PORT, decode_responses=True)

# --- Step 1: Insert values 1-100 into source-db with lists ---
source_r.delete("list_numbers")
for i in range(1, 101):
    source_r.rpush("list_numbers", i)
  
print("Inserted values 1-100 into source-db.")

# --- Step 2: Read values in reverse order from replica-db ---
print("\nList - reverse order:")

values = replica_r.lrange("list_numbers", 0, -1)
for v in reversed(values):
    print(v,end=' ')

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

# --- Step 1: Insert values 1-100 into source-db ---
for i in range(1, 101):
    key = f"key:{i}"
    source_r.set(key, i)
  
print("Inserted values 1-100 into source-db.")

# --- Step 2: Read values in reverse order from replica-db ---
print("Reading values from replica-db in reverse order:")

for i in range(100, 0, -1):
    key = f"key:{i}"
    value = replica_r.get(key)
    print(value, end=' ')
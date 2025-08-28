#!/usr/bin/env python3
import redis
# Source and replica Redis connection details
SOURCE_HOST = "redis-13249.re-cluster1.ps-redislabs.org"
SOURCE_PORT = 13249

REPLICA_HOST = "redis-13592.re-cluster1.ps-redislabs.org"
REPLICA_PORT = 13592

# Connect to source Redis
source_r = redis.Redis(host=SOURCE_HOST, port=SOURCE_PORT, decode_responses=True)
# Connect to replica Redis
replica_r = redis.Redis(host=REPLICA_HOST, port=REPLICA_PORT, decode_responses=True)

# --- Step 1: Insert values 1-100 into source-db with lists ---
source_r.delete("numbers")
for i in range(1, 101):
    source_r.rpush("numbers", i)
  
print("Inserted values 1-100 into source-db.")

# --- Step 2: Read values in reverse order from replica-db ---
print("\nList - reverse order:")

values = replica_r.lrange("numbers", 0, -1)
for v in reversed(values):
    print(v)

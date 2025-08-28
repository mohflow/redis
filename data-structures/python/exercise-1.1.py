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

# --- Step 1: Insert values 1-100 into source-db ---
for i in range(1, 101):
    key = f"num:{i}"
    source_r.set(key, i*2)
  
print("Inserted values 1-100 into source-db.")

# --- Step 2: Read values in reverse order from replica-db ---
print("Reading values from replica-db in reverse order:")

for i in range(10, 0, -1):
    key = f"num:{i}"
    value = replica_r.get(key)
    print(f"{key} -> {value}")

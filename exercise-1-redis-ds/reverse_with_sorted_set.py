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

print("--- Using Sorted Set ---")
zset_key = 'numbers_zset'
source_r.delete(zset_key)

for i in range(1, 101):
    source_r.zadd(zset_key, {str(i): i})

values = replica_r.zrevrange(zset_key, 0, -1)
print("Reverse order from replica-db:")
for val in values:
    print(val, end=' ')
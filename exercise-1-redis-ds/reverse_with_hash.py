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

print("--- Using Hash ---")
hash_key = 'numbers_hash'
source_r.delete(hash_key)

for i in range(1, 101):
    source_r.hset(hash_key, f'num{i}', i)

fields = [f'num{i}' for i in range(100, 0, -1)]
values = replica_r.hmget(hash_key, fields)
print("Reverse order from replica-db:")
for field, value in zip(fields, values):
    print(f'{field}: {value}', end=' ')
    print("\n")
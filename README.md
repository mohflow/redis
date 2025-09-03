# Redis Exercises

This repository contains a series of Redis exercises designed to help you learn and practice Redis operations, REST API integration, and semantic routing.

## Exercises

1. **Exercise 1: Redis Data Structures**  
   Learn how to create a Redis database from Redis Enterprise cluster UI and insert values from 1 to 100. This exercise also demonstrates how to read the values in reverse order.  
   [View Instructions](https://github.com/mohflow/redis/blob/main/exercise-1-redis-ds/README.md)

   The load node has the memtier_benchmark command at /tmp/memtier_benchmark.txt
   ```bash
   memtier_benchmark -s  redis-17890.re-cluster1.ps-redislabs.org -p 17890 --threads=4 --clients=50 --requests 10000 --data-size 128 --ratio=1:0
   ```
3. **Exercise 2: REST API with Redis**  
   This exercise guides you through creating a Redis database, setting up roles and users, listing users, and deleting the database via a REST API.  
   [View Instructions](https://github.com/mohflow/redis/tree/main/exercise-2-rest-api/README.md)

4. **Bonus Exercise: Semantic Routing**  
   Explore Redis Semantic Routing with a hands-on exercise.  
   [View Instructions](https://github.com/mohflow/redis/blob/main/semantic-routing-bonus-exercise/README.md)

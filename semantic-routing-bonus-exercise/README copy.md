# Redis Semantic Routing Demo

This project demonstrates **semantic routing** using **Redis** as the vector database and [`redisvl`](https://github.com/redis/redis-vl-python) as the semantic router framework.

Reference: [redis-vl semantic router guide](https://github.com/redis/redis-vl-python/blob/main/docs/user_guide/08_semantic_router.ipynb)

---

## 🚀 Prerequisites

* Python 3.8+
* A Redis deployment with the following modules enabled:

  * **RediSearch**
  * **ReJSON**
* Access credentials to your Redis cluster

---

## ⚙️ Setup

1. Install dependencies:

   ```bash
   pip install redis redisvl
   ```

2. (Optional) Verify that Redis modules are loaded:

   ```bash
   rladmin status modules
   curl -k -u "admin@rl.org:wPDMWL0" https://re-cluster1.ps-redislabs.org:9443/v1/modules
   ```

3. Create the Redis database with required modules:

   ```bash
   python3 create_db.py
   ```

4. Initialize the semantic router and persist routes to Redis:

   ```bash
   python3 routes_setup.py
   ```

5. Verify the router index exists in Redis:

   ```bash
   rvl index info -i topic_router --url redis://redis-15000.re-cluster1.ps-redislabs.org:15000
   ```

6. (Optional) Inspect the keys and vectors using [RedisInsight](https://redis.io/insight/).

---

## 🔍 Querying

Run the query script to find the best-matching route for your input:

```bash
python3 query.py
```

Example output:

```
sci_fi_entertainment
genai_programming
classical_music
```

---

## 📂 Files

* `create_db.py` → creates the database with required modules
* `routes_setup.py` → defines routes and persists them to Redis
* `query.py` → attaches to the existing router and runs queries

---

👉 With this flow, you only need to run `routes_setup.py` once. After that, you can run `query.py` as many times as you like — the router index is persisted inside Redis.

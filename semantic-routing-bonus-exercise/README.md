# redis

This challenge is to demonstrate semanticRouting using Redis DB and Redisvl Semantic Router.

https://github.com/redis/redis-vl-python/blob/main/docs/user_guide/08_semantic_router.ipynb

# Solution

To run the rvl commands locally
1. pip install redis
2. pip install redisvl
3. Get the redis versions using commands 'rladmin status modules' and 'curl -k -u "admin@rl.org:wPDMWL0" https://re-cluster1.ps-redislabs.org:9443/v1/modules'
4. run create_db.py to create the database with modules Redisearch and ReJson 
5. run the routes_setup.py to initialize the semanticrouter with router and to store the routes in redis
6. run the command to verify if the router is persisted into redis db 'rvl index info -i topic_router --url redis://redis-15000.re-cluster1.ps-redislabs.org:15000'
7. You may also verify the routes/keys on Redis insights by adding the db 
8. Finally run the query.py to get the best routes for the requests.
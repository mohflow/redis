import requests
import json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# === Suppress insecure HTTPS warnings ===
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# === Load Config ===
with open("/home/coder/redis/semantic-routing-bonus-exercise/config.json", "r") as f:
    config = json.load(f)

REST_URL = config["rest_url"]
USERNAME = config["username"]
PASSWORD = config["password"]

# ===== CHECK IF DB ALREADY EXISTS ELSE CREATE DATABASE ===

DB_NAME = "semantic-router-db"

db_list_resp = requests.get(
    f"{REST_URL}/v1/bdbs",
    auth=HTTPBasicAuth(USERNAME, PASSWORD),
    verify=False
)
db_list = db_list_resp.json()

existing_db = next((db for db in db_list if db["name"] == DB_NAME), None)

if existing_db:
    print(f"Database '{DB_NAME}' already exists with ID: {existing_db['uid']}")
    DB_ID = existing_db["uid"]
else:
    db_payload = {
    "name": DB_NAME,
    "memory_size": 1073741824,  # 1GB
    "type": "redis",
    "port": 15000,
    "shards_count": 1,
    "oss_cluster": False,
    "module_list": [
        {"module_name": "search", "semantic_version": "2.10.12", "module_args": ""},
        {"module_name": "ReJSON", "semantic_version": "2.8.8", "module_args": ""}
    ]
    }

    db_resp = requests.post(
        f"{REST_URL}/v1/bdbs",
        json=db_payload,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        verify=False  
    )

    if db_resp.status_code == 200:
        DB_ID = db_resp.json()["uid"]
        print(f"Database '{DB_NAME}' created successfully with ID: {DB_ID}")
    else:
        print("Failed to create database:", db_resp.status_code, db_resp.text)


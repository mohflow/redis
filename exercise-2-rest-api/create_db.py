import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

# === Suppress insecure HTTPS warnings ===
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# === Load config ===
with open("/home/coder/redis/exercise-2-rest-api/config.json", "r") as f:
    config = json.load(f)

REST_URL = config["rest_url"]
USERNAME = config["username"]
PASSWORD = config["password"]

# ========= CREATE DATABASE =========

DB_NAME = "rest-api-db"

# === Check if DB exists ===
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
    "port": 12000,
    "shards_count": 1,
    "oss_cluster": False
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


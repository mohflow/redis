import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import create_roles

# === Suppress insecure HTTPS warnings ===
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# === Load config ===
with open("/home/coder/redis/exercise-2-rest-api/config.json", "r") as f:
    config = json.load(f)

REST_URL = config["rest_url"]
USERNAME = config["username"]
PASSWORD = config["password"]

# ========== CHECK IF ROLES (admin,db_viewer,db_member) ALREADY EXIST, ELSE CREATE ========

create_roles.ensure_roles_exist()

# ========= CREATE USERS =========
with open("/home/coder/redis/exercise-2-rest-api/users.json", "r") as f:
    users = json.load(f)

for user in users:
    resp = requests.post(
        f"{REST_URL}/v1/users",
        json=user,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        verify=False
    )
    print(f"User {user['email']} creation status:", resp.status_code)
    try:
        print(resp.json())
    except Exception:
        print("No JSON response, raw text:", resp.text)

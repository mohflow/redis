import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

# === Suppress insecure HTTPS warnings ===
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# === Load config ===
with open("config.json", "r") as f:
    config = json.load(f)

REST_URL = config["rest_url"]
USERNAME = config["username"]
PASSWORD = config["password"]


# === DB NAME ===
DB_NAME = "rest-api-db"  

# === Delete database function ===
def delete_database(db_name):
    # Redis Enterprise API uses database UID, so first we need to fetch it
    dbs_url = f"{REST_URL}/v1/bdbs"
    response = requests.get(dbs_url, auth=(USERNAME, PASSWORD), verify=False)
    response.raise_for_status()
    databases = response.json()

    # Find the database UID
    db_uid = None
    for db in databases:
        if db.get("name") == db_name:
            db_uid = db.get("uid")
            break

    if not db_uid:
        print(f"Database '{db_name}' not found!")
        return

    # Delete the database
    delete_url = f"{REST_URL}/v1/bdbs/{db_uid}"
    delete_resp = requests.delete(delete_url, auth=(USERNAME, PASSWORD), verify=False)
    if delete_resp.status_code == 200:
        print(f"Database '{db_name}' deleted successfully.")
    else:
        print(f"Failed to delete database '{db_name}': {delete_resp.status_code} {delete_resp.text}")

# === Main ===
if __name__ == "__main__":
    delete_database(DB_NAME)
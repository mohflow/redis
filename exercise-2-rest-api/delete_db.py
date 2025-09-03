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
    # Prompt user for database name and ensure it's not empty
    while True:
        db_name = input("Enter the name of the database you want to delete: ").strip()
        if db_name:
            break
        print("Database name cannot be empty. Please enter a valid name.")

    # Confirm deletion
    while True:
        confirm = input(f"Are you sure you want to delete the database '{db_name}'? (yes/no): ").strip().lower()
        if confirm in ("yes", "no"):
            break
        print("Invalid input. Please type 'yes' or 'no'.")

    if confirm == "yes":
        delete_database(db_name)
    else:
        print("Database deletion cancelled.")
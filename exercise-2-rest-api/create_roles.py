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


# Roles you want to ensure exist
TARGET_MANAGEMENT_ROLES = ["admin", "db_member", "db_viewer"]

# ==== Helper functions ====

def get_roles():
    """
    Fetch all existing roles from the Redis REST API.
    Returns a list of role dicts.
    """
    url = f"{REST_URL}/v1/roles"
    response = requests.get(url, auth=(USERNAME, PASSWORD), headers={"Accept": "application/json"}, verify=False)
    response.raise_for_status()
    return response.json()

def create_role(name, management):
    """
    Create a new role.
    management must be one of approved strings (e.g. 'admin', 'db_member', 'db_viewer', etc.)
    """
    url = f"{REST_URL}/v1/roles"
    payload = {"name": name, "management": management}
    response = requests.post(
        url,
        auth=(USERNAME, PASSWORD),
        headers={"Content-Type": "application/json"},
        json=payload,
        verify=VERIFY_SSL
    )
    if response.status_code == 200:
        print(f"Successfully created role: name='{name}', management='{management}'")
        return response.json()
    else:
        print(f"Failed to create role '{name}': {response.status_code} {response.text}")
        response.raise_for_status()

def ensure_roles_exist():
    """
    Ensure each target management role exists; create any that don't.
    """
    existing_roles = get_roles()
    existing_managements = {r.get("management") for r in existing_roles}
    # For debugging:
    print(f"Existing management roles: {existing_managements}")
    for mgmt in TARGET_MANAGEMENT_ROLES:
        if mgmt not in existing_managements:
            print(f"Role with management '{mgmt}' not found — creating...")
            create_role(name=mgmt.capitalize().replace("_", " "), management=mgmt)
        else:
            print(f"Role with management '{mgmt}' already exists.")

# === Run ===
if __name__ == "__main__":
    ensure_roles_exist()

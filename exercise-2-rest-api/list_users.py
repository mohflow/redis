import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

# === Load config ===
with open("config.json", "r") as f:
    config = json.load(f)

REST_URL = config["rest_url"]
USERNAME = config["username"]
PASSWORD = config["password"]

# === Suppress insecure HTTPS warnings ===
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# === Fetch all users ===
def get_users():
    url = f"{REST_URL}/v1/users"
    response = requests.get(
        url,
        auth=(USERNAME, PASSWORD),
        headers={"Accept": "application/json"},
        verify=False
    )
    # response.raise_for_status()
    return response.json()  # Returns a list of user dicts

# === Display users in desired format ===
def display_users(users):
    print(f"{'Name':<20} {'Role':<15} {'Email'}")
    print("-" * 64)
    for user in users:
        name = user.get("name", "N/A")
        role = user.get("role", "N/A")
        email = user.get("email", "N/A")
        print(f"{name:<20} {role:<15} {email}")

# === Main ===
if __name__ == "__main__":
    users = get_users()
    display_users(users)

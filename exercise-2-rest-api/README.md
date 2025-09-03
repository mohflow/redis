# Redis REST API Automation Script

This repository contains a script that interacts with Redis using the REST API to perform various operations. The script includes functionalities such as creating a new database, adding users with specific roles, listing and displaying users, and deleting the created database.

---

## Prerequisites

* Redis REST API endpoint: `https://re-cluster1.ps-redislabs.org:9443` (Use IP address if the hostname isn't resolving)
* REST API credentials (username and password)
* Python 3.x installed (or your preferred language runtime)
* Internet connectivity to access the Redis REST API

---

## REST API Documentation

Full Redis REST API documentation can be found [here](https://docs.redislabs.com/latest/rs/references/rest-api/).

---

## Script Features

The script performs the following steps:

1. **Create Database**

   * Uses the Redis Database API to create a new database.
   * Does not use any external modules; utilizes standard libraries only (e.g., `requests` in Python).

2. **Create Users**

   * Adds three users to the newly created database:

     | Name         | Email                                                       | Role       |
     | ------------ | ----------------------------------------------------------- | ---------- |
     | John Doe     | [john.doe@example.com](mailto:john.doe@example.com)         | db\_viewer |
     | Mike Smith   | [mike.smith@example.com](mailto:mike.smith@example.com)     | db\_member |
     | Cary Johnson | [cary.johnson@example.com](mailto:cary.johnson@example.com) | admin      |

3. **List and Display Users**

   * Fetches all users using the Users API.
   * Displays the users in a readable format: **Name | Role | Email**.

4. **Delete Database**

   * Deletes the previously created database using the Database API.

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/mohflow/redis.git
cd redis/exercise-2-rest-api
```

2. Update configuration (if required):

```json
{
    "rest_url": "https://re-cluster1.ps-redislabs.org:9443",
    "username": "<your-username>",
    "password": "<your-password>"
}
```

3. Create database:

```bash
python3 create_db.py
```

4. Create Users which checks if roles exists , if not creates the roles before creating the users:

```bash
python3 create_users.py
```
5. Display users

```bash
python3 list_users.py
```

6. Delete the database created

```bash
python3 delete_db.py
```

7. Check the console output to verify database creation, user creation, and user listing.

---


## Notes

* Ensure the REST API endpoint is reachable and credentials are correct.
* Use IP address if DNS resolution for the host fails.
* The script can be adapted to other languages such as Java, Go, or JavaScript by replacing HTTP request logic accordingly.

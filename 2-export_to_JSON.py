#!/usr/bin/python3
import requests
import sys
import json


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user info
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch todos
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Build required JSON structure
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    final_data = {
        employee_id: tasks_list
    }

    # Write to USER_ID.json
    filename = f"{employee_id}.json"

    with open(filename, mode="w") as json_file:
        json.dump(final_data, json_file)
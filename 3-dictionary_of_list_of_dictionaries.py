#!/usr/bin/python3
import requests
import json


if __name__ == "__main__":

    # API endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users
    users_response = requests.get(users_url)
    users = users_response.json()

    # Fetch all todos
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Dictionary to store final data
    final_data = {}

    # Loop through each user
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        # Create list of tasks for this user
        user_tasks = []

        for task in todos:
            if task.get("userId") == user.get("id"):
                user_tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

        final_data[user_id] = user_tasks

    # Write to file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(final_data, json_file)
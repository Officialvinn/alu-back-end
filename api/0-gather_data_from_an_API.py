#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    # Check if employee ID was provided
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    # API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Get employee info
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]

    # Print result
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")
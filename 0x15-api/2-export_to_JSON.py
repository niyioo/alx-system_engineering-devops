#!/usr/bin/python3
"""
Retrieve and display an employee's TODO list progress from a REST API
and export in JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'

    employee_id = sys.argv[1]

    user_url = f'{base_url}users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username')

    print(f"Employee {username} is done with tasks", end="")

    todo_url = f'{base_url}todos?userId={employee_id}'
    todo_response = requests.get(todo_url)
    tasks = todo_response.json()

    completed_tasks = [{"task": task["title"], "completed": task["completed"], "username": username} for task in tasks if task["completed"]]

    user_json = {employee_id: completed_tasks}

    json_file_name = f"{employee_id}.json"

    with open(json_file_name, 'w') as json_file:
        json.dump(user_json, json_file)

    print(f"({len(completed_tasks)}/{len(tasks)}):")

    for task in completed_tasks:
        print(f"\t {task['task']}")

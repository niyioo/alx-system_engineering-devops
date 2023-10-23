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

    user_url = '{}users/{}'.format(base_url, employee_id)
    user_response = requests.get(user_url)
    u_data = user_response.json()

    print("Employee {} is done with tasks".format(u_data.get('name')), end="")

    todo_url = '{}todos?userId={}'.format(base_url, employee_id)
    todo_response = requests.get(todo_url)
    tasks = todo_response.json()

    task_list = []
    for task in tasks:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": u_data.get("username")
        }
        task_list.append(task_info)

    task_dict = {str(employee_id): task_list}
    json_file_name = '{}.json'.format(employee_id)

    with open(json_file_name, 'w') as json_file:
        json.dump(task_dict, json_file)

#!/usr/bin/python3
"""
Task #0: Retrieve and display an employee's TODO list progress from a REST API
"""
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

    completed_tasks = [task for task in tasks if task.get('completed') is True]

    print("({}/{}):".format(len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

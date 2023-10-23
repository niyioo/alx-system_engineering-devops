#!/usr/bin/python3
"""
Task #3: Dictionary of list of dictionaries
"""
import json
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Initialize a dictionary to store tasks for all employees
    all_tasks = {}

    for employee_id in range(1, 11):  # Assuming employee IDs from 1 to 10
        user_url = '{}users/{}'.format(base_url, employee_id)
        user_response = requests.get(user_url)
        user_data = user_response.json()
        username = user_data.get('username')

        todo_url = '{}todos?userId={}'.format(base_url, employee_id)
        todo_response = requests.get(todo_url)
        tasks = todo_response.json()

        task_list = []
        for task in tasks:
            task_info = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            task_list.append(task_info)

        all_tasks[str(employee_id)] = task_list

    # Export the all_tasks dictionary in JSON format
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)

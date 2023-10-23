#!/usr/bin/python3
"""
This script retrieves and displays an employee's TODO list
progress from a REST API.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{employee_id}'
    todo_url = f'{base_url}todos?userId={employee_id}'

    try:
        # Retrieve user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Retrieve TODO list for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Calculate TODO list progress
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task['completed'])

        # Display progress
        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, completed_tasks, total_tasks))
        for task in todo_data:
            if task['completed']:
                print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(int(employee_id))

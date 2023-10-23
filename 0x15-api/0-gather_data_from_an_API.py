#!/usr/bin/python3
"""
Task #0: Retrieve and display an employee's TODO list progress from a REST API
"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]

    user_url = f'{url}users/{user_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_name = user_data.get('name')

    todo_url = f'{url}todos?userId={user_id}'
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    num_todos = len(todos)
    num_completed = len([todo for todo in todos if todo.get("completed")])

    print(f"Employee {user_name} is done with {num_completed}/{num_todos} "
          f"tasks:")
    for todo in todos:
        if todo.get("completed"):
            print(f"\t{todo.get('title')}")

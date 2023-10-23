#!/usr/bin/python3
"""
This script retrieves and exports an employee's TODO list
progress from a REST API to a CSV file.
"""
import csv
import requests
import sys


def get_employee_todo_progress_to_csv(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{employee_id}'
    todo_url = f'{base_url}todos?userId={employee_id}'

    try:
        # Retrieve user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        user_id = user_data.get('id')
        user_name = user_data.get('name')

        # Retrieve TODO list for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Prepare CSV file name
        csv_file_name = f"{user_id}.csv"

        # Write data to CSV file
        with open(csv_file_name, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
            ])

            for task in todo_data:
                csv_writer.writerow([
                    user_id,
                    user_name,
                    task['completed'],
                    task['title']
                ])

        print(f"Data has been exported to {csv_file_name}")

    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress_to_csv(int(employee_id))

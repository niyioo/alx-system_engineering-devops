#!/usr/bin/python3
""" Retrieve and display an employee's TODO list progress from a
REST API and export in CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'

    employee_id = sys.argv[1]

    user_url = '{}users/{}'.format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username')

    print("Employee {} is done with tasks".format(username), end="")

    todo_url = '{}todos?userId={}'.format(base_url, employee_id)
    todo_response = requests.get(todo_url)
    tasks = todo_response.json()

    task_list = []
    for task in tasks:
        task_list.append([employee_id,
                          username,
                          task.get('completed'),
                          task.get('title')])

    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in task_list:
            employee_writer.writerow(task)

#!/usr/bin/python3
"""Script that retrieves employee data using REST API."""

import csv
import requests
from sys import argv


def get_employee_data(employee_id):
    """
    Retrieve employee data and print their completed tasks.
    """

    BASE_URL = "https://jsonplaceholder.typicode.com/"
    EMP_ENDPOINT = BASE_URL + "users/{}".format(employee_id)

    emp_data = requests.get(EMP_ENDPOINT).json()

    TASKS_ENDPOINT = BASE_URL + 'todos?userId={}'.format(emp_data["id"])
    tasks_data = requests.get(TASKS_ENDPOINT).json()
    data = {"employee": emp_data, "tasks": tasks_data}

    with open('{}.csv'.format(argv[1]), 'w') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        emp_username = data['employee']['username']
        emp_id = data['employee']['id']

        for task in data['tasks']:
            w.writerow([emp_username, emp_id, task[
                "completed"], task["title"]])


if __name__ == "__main__":
    employee_id = argv[1]
    get_employee_data(employee_id)

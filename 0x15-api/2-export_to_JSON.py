#!/usr/bin/python3
"""Script that retrieves employee data using REST API."""

import json
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
    emp_id = data['employee']['id']
    temp = []
    for task in data['tasks']:
        emp_data = {}
        emp_data['task'] = task['title']
        emp_data['completed'] = task['completed']
        emp_data['username'] = data['employee']['username']
        temp.append(emp_data)
        emp_total = {emp_id: temp}
        with open('{}.json'.format(emp_id), 'w') as f:
            json.dump(emp_total, f)


if __name__ == "__main__":
    employee_id = argv[1]
    get_employee_data(employee_id)

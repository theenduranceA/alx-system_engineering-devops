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

    TASKS_ENDPOINT = BASE_URL + 'todos?userId={}'.format(emp_data.get("id"))
    tasks_data = requests.get(TASKS_ENDPOINT).json()
    data = {"employee": emp_data, "tasks": tasks_data}

    csv_filename = '{}.csv'.format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        username = data['employee']['username']
        user_id = data['employee']['id']

        csv_writer.writerow([
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in data['tasks']:
            csv_writer.writerow([emp_data["id"], emp_data["name"], task[
                "completed"], task["title"]])


if __name__ == "__main__":
    employee_id = argv[1]
    get_employee_data(employee_id)

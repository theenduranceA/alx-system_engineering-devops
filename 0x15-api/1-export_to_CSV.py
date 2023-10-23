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

    total_tasks = len(tasks_data)
    completed_tasks = [task for task in tasks_data if task["completed"]]

    print("Employee {} has completed {}/{} tasks:"
          .format(emp_data["name"], len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print('\t {}'.format(task["title"]))

    csv_filename = '{}.csv'.format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in completed_tasks:
            csv_writer.writerow([emp_data["id"], emp_data["name"], task[
                "completed"], task["title"]])


if __name__ == "__main__":
    employee_id = argv[1]
    get_employee_data(employee_id)

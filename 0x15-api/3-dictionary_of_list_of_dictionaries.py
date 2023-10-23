#!/usr/bin/python3
"""Script that retrieves employee data using REST API."""

import json
import requests


def get_all_employee_data():
    """Retrieve employee data and print their completed tasks."""

    BASE_URL = "https://jsonplaceholder.typicode.com/"

    users_data = requests.get(BASE_URL + "users").json()
    tasks_data = requests.get(BASE_URL + "todos").json()

    tot_data = {}

    for user in users_data:
        temp = []
        for task in tasks_data:
            if user["id"] == task["userId"]:
                emp_task = {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user["username"]
                }
                temp.append(emp_task)
        tot_data[user["id"]] = temp

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(tot_data, json_file)


if __name__ == "__main__":
    get_all_employee_data()

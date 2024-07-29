#!/usr/bin/python3
"""
Returns information about a TODO list progress,
for a given employee's ID using REST API,
and exports data in the JSON format.
"""
import json
import requests


def main():
    """
    Returning employee's TODO list informations,
    and exporting JSON data.
    """
    id = 1
    dt_dict = {}
    while True:
        url = "https://jsonplaceholder.typicode.com/"
        users = f'users?id={id}'
        todos = f'todos?userId={id}'
        userData = requests.get(f'{url}{users}').json()
        if not userData:
            break
        userName = userData[0].get("username")
        todosData = requests.get(f'{url}{todos}').json()
        dt_dict[id] = [
                {
                    "username": userName,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                for task in todosData
            ]
        id += 1
    with open("todo_all_employees.json", "w") as f:
        json.dump(dt_dict, f)


if __name__ == "__main__":
    main()

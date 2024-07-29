#!/usr/bin/python3
"""
Returns information about a TODO list progress,
for a given employee's ID using REST API,
and exports data in the JSON format.
"""
import json
import requests
import sys


def main():
    """
    Returning employee's TODO list informations,
    and exporting JSON data.
    """
    id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'
    users = f'users?id={id}'
    todos = f'todos?userId={id}'
    done = f'{todos}&completed=true'
    notDone = f'{todos}&completed=false'
    userData = requests.get(f'{url}{users}').json()
    Name = userData[0].get("name")
    userName = userData[0].get("username")
    todosData = requests.get(f'{url}{todos}').json()
    todosDone = requests.get(f'{url}{done}').json()
    doneN = len(todosDone)
    totalN = len(todosData)
    with open(f'{id}.json', 'w') as f:
        data = {
            id: [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": userName,
                }
                for task in todosData
            ]
        }
        json.dump(data, f)


if __name__ == "__main__":
    main()

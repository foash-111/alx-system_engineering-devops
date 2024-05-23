#!/usr/bin/python3
"""
make a get request and come back with json response
"""

import json
import requests
import sys


def main():
    response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    response_users = requests.get("https://jsonplaceholder.typicode.com/users")

    users_dict = {}

    if response_users.headers.get('Content-Type')\
            .startswith("application/json") and\
            response_todos.headers.get('Content-Type')\
            .startswith("application/json"):

        users_data = response_users.json()
        todos_data = response_todos.json()
        for user in users_data:
            my_list = []
            for todo in todos_data:
                if user.get('id') == todo.get('userId'):
                    inner_dict = {}
                    inner_dict['username'] = user.get('username')
                    inner_dict['completed'] = todo.get('completed')
                    inner_dict['task'] = todo.get('title')
                    my_list.append(inner_dict)

            users_dict[f"{user.get('id')}"] = my_list

    with open("todo_all_employees.json", 'w+') as file:
        json.dump(users_dict, file)


if __name__ == "__main__":
    main()

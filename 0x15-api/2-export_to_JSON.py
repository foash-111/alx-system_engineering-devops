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

    my_list = []
    user_name = ""
    user_dict = {f"{sys.argv[1]}": []}
    inner_dict = {'task': '', 'completed': "", 'username': ''}

    if response_users.headers.get('Content-Type')\
            .startswith("application/json"):

        users_data = response_users.json()
        for x in users_data:
            if x.get('id') == int(sys.argv[1]):
                user_name = x.get('username')
                break
    inner_dict['username'] = user_name

    if response_todos.headers.get('Content-Type')\
            .startswith("application/json"):

        todos_data = response_todos.json()
        for x in todos_data:
            if x.get('userId') == int(sys.argv[1]):
                inner_dict['completed'] = x.get('completed')
                inner_dict['task'] = x.get('title')
                user_dict[f"{sys.argv[1]}"].append(inner_dict)

    with open("{}.json".format(sys.argv[1]), 'w+') as file:
        json.dump(user_dict, file)


if __name__ == "__main__":
    main()

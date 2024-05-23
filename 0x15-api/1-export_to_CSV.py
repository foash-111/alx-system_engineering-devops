#!/usr/bin/python3
"""
make a get request and come back with json response
"""

import csv
import requests
import sys


def main():
    response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    response_users = requests.get("https://jsonplaceholder.typicode.com/users")

    my_list = []
    user_name = ""

    if response_todos.headers.get('Content-Type')\
            .startswith("application/json"):

        todos_data = response_todos.json()
        for x in todos_data:
            if x.get('userId') == int(sys.argv[1]):
                inner_list = []
                inner_list.append(x.get('completed'))
                inner_list.append(x.get('title'))
                my_list.append(inner_list)

    if response_users.headers.get('Content-Type')\
            .startswith("application/json"):

        users_data = response_users.json()
        for x in users_data:
            if x.get('id') == int(sys.argv[1]):
                user_name = x.get('username')

    with open("{}.csv".format(sys.argv[1]), 'w+') as file:
    
        for x in my_list:
            file.write(f'"{sys.argv[1]}","{user_name}","{x[0]}","{x[1]}"\n')


if __name__ == "__main__":
    main()

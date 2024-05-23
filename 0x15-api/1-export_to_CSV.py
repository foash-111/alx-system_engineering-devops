#!/usr/bin/python3
"""
make a get request and come back with json response
"""


import requests
import sys
import csv


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
                user_name = x.get('name')

    with open("{}.csv".format(sys.argv[1]), 'a+', newline='') as file:
        writer = csv.writer(file)
        for x in my_list:
            writer.writerow([sys.argv[1], user_name, ','.join(map(str, x))])


if __name__ == "__main__":
    main()

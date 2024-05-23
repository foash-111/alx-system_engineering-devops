#!/usr/bin/python3

import requests
import sys

"""make a get request and come back with json response"""


response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
response_users = requests.get("https://jsonplaceholder.typicode.com/users")

completed_tasks = 0
uncompleted_tasks = 0
my_list = []
user_name = ""

if response_todos.headers.get('Content-Type').startswith("application/json"):
    todos_data = response_todos.json()
    for x in todos_data:
        if x.get('userId') == int(sys.argv[1]):
            if x.get('completed') is True:
                completed_tasks += 1
                my_list.append(x.get('title'))
            else:
                uncompleted_tasks += 1

total_num_of_tasks = completed_tasks + uncompleted_tasks


if response_users.headers.get('Content-Type').startswith("application/json"):
    users_data = response_users.json()
    for x in users_data:
        if x.get('id') == int(sys.argv[1]):
            user_name = x.get('name')


print(
    'Employee {} is done with tasks({}/{}):'
    .format(user_name, completed_tasks, total_num_of_tasks)
    )
for to_do in my_list:
    print("\t ", to_do)

#!/usr/bin/python3
"""
This module makes GET requests to the JSON Placeholder API
to retrieve TODO lists and user details,
Usage: Provide the employee ID as a command-line argument.
"""

import requests
import sys

# Fetching TODO lists and user details from the JSONPlaceholder API
response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
response_users = requests.get("https://jsonplaceholder.typicode.com/users")

# Initialize counters and lists
completed_tasks = 0
uncompleted_tasks = 0
my_list = []
user_name = ""

# Check if the response content type is JSON
if response_todos.headers.get('Content-Type').startswith("application/json"):
    todos_data = response_todos.json()
    # Iterate through the TODO items
    for x in todos_data:
        # Filter by employee ID passed as a command-line argument
        if x.get('userId') == int(sys.argv[1]):
            # Increment completed tasks counter if the task is completed
            if x.get('completed') is True:
                completed_tasks += 1
                my_list.append(x.get('title'))
            # Otherwise, increment uncompleted tasks counter
            else:
                uncompleted_tasks += 1

# Calculate the total number of tasks
total_num_of_tasks = completed_tasks + uncompleted_tasks

# Fetch user details
if response_users.headers.get('Content-Type').startswith("application/json"):
    users_data = response_users.json()
    # Find the user matching the provided employee ID
    for x in users_data:
        if x.get('id') == int(sys.argv[1]):
            user_name = x.get('name')

# Display the employee's TODO list progress
print(
    'Employee {} is done with tasks({}/{}):'
    .format(user_name, completed_tasks, total_num_of_tasks)
    )
# Print each task title
for to_do in my_list:
    print("\t", to_do)

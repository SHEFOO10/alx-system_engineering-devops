#!/usr/bin/python3
""" using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import json
import requests
import sys


def get_users():
    """ get user object """
    users = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    return users


def get_todos(user_id):
    """ returns information about his/her TODO list progress. """
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(user_id)).json()
    return todos


def export_to_json(users):
    """ export todos associated with the given user id """
    with open('todo_all_employees.json', 'w') as jsonfile:
        all_users_todos = {}
        for user in users:
            user_id = user.get('id')
            user_todos = {"{}".format(user_id): []}
            for todo in get_todos(user_id):
                user_todos['{}'.format(user_id)].append({
                    "username": user.get('username'),
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                })
            all_users_todos.update(user_todos)
        json.dump(all_users_todos, jsonfile)


if __name__ == "__main__":
    users = get_users()
    export_to_json(users)

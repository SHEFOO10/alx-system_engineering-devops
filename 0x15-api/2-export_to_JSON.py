#!/usr/bin/python3
""" using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import json
import requests
import sys


def get_user(user_id):
    """ get user object """
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)
                        ).json()
    return user


def get_todo(user_id):
    """ returns information about his/her TODO list progress. """
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(user_id)).json()
    do_with = []
    for todo in todos:
        if todo.get('completed') is True:
            do_with.append(todo)
    return (do_with, todos)


def export_to_json(todos, user):
    """ export todos associated with the given user id """
    user_id = user.get('id')
    with open('{}.json'.format(user_id), 'w') as jsonfile:
        user_todos = {"{}".format(user_id): []}
        for todo in todos:
            user_todos["{}".format(user_id)].append({
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": user.get('username')
            })
        json.dump(user_todos, jsonfile)


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = get_user(user_id)
    done_with, todos = get_todo(user_id)
    export_to_json(todos, user)

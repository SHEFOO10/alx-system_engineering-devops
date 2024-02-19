#!/usr/bin/python3
""" using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import csv
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


def export_to_csv(todos, user):
    """ export todos associated with the given user id """
    with open('{}.csv'.format(user.get('id')), 'w') as csvfile:
        for todo in todos:
            csvfile.write('"{}","{}","{}","{}"\n'
                          .format(
                            user.get('id'),
                            user.get('username'),
                            todo.get('completed'),
                            todo.get('title')
                            )
                          )


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = get_user(user_id)
    done_with, todos = get_todo(user_id)
    export_to_csv(todos, user)

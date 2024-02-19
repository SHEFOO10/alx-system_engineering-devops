#!/usr/bin/python3
""" using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests
import sys


def get_user(user_id):
    """ get user object """
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={'id': '{}'.format(sys.argv[1])}
                        ).json()[0]
    return user


def get_todo(user_id):
    """ returns information about his/her TODO list progress. """
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': '{}'.format(sys.argv[1])}
                         ).json()
    do_with = []
    for todo in todos:
        if todo.get('completed') is True:
            do_with.append(todo)
    return (do_with, todos)


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = get_user(user_id)
    done_with, todos = get_todo(user_id)

    print('Employee {} is done with tasks({}/{}):'
          .format(user.get('name'), len(done_with), len(todos))
          )
    for todo_done in done_with:
        print('\t {}'.format(todo_done.get('title')))

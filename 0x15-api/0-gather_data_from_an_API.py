#!/usr/bin/python3
""" """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    else:
        uID = sys.argv[1]
        ToDo_URL = "https://jsonplaceholder.typicode.com/todos"
        User_URL = "https://jsonplaceholder.typicode.com/users/{}".format(uID)

        Todo_r = requests.get(ToDo_URL)
        User = requests.get(User_URL)
        reponse = User.json()
        Todo_j = Todo_r.json()
        count = 0
        completed = 0
        for todo in Todo_j:
            if todo.get('userId') == int(uID):
                title = todo.get('title')
                count += 1
                if todo.get('completed') is True:
                    completed += 1

        print("Employee {} is done with tasks({}/{}):".format(
            reponse.get('name'), completed, count
        ))
        for task in Todo_j:
            if task.get('userId') == int(uID):
                if task.get('completed') is True:
                    print(f"\t {task.get('title')}")

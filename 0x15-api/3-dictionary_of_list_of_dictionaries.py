#!/usr/bin/python3
"""Python Script Same As Task#0 But Export All Data in Dictionnary"""

import json
import requests


if __name__ == "__main__":
    ToDo_URL = "https://jsonplaceholder.typicode.com/todos"
    User_URL = "https://jsonplaceholder.typicode.com/users"

    Todo_r = requests.get(ToDo_URL)
    Todo_j = Todo_r.json()
    formatted_data = {}
    for item in Todo_j:
        user_id = item.get('userId')
        User = requests.get(User_URL + "/{}".format(user_id))
        reponse = User.json()
        task = {"task": item.get('title'),
                "completed": item.get('completed'),
                "username": reponse.get('username')}

        if user_id not in formatted_data:
            formatted_data[user_id] = [task]
        else:
            formatted_data[user_id].append(task)
    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(formatted_data, json_file)

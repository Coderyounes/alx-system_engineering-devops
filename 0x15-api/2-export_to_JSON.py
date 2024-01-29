#!/usr/bin/python3
"""Python Script Same As Task#0 But Export data in JSon"""

import requests
import json
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
        formatted_data = {}
        for item in Todo_j:
            if item.get('userId') == int(uID):
                user_id = item.get('userId')
                task = {"task": item.get('title'),
                        "completed": item.get('completed'),
                        "username": reponse.get('username')}

                if user_id not in formatted_data:
                    formatted_data[user_id] = [task]
                else:
                    formatted_data[user_id].append(task)
        with open("{}.json".format(uID), mode='w') as json_file:
            json.dump(formatted_data, json_file)

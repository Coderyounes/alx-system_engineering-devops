#!/usr/bin/python3
""" Python Script Same as the Previous one But Expot Data as CSV """
import csv
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

    with open("{}.csv".format(uID), mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for Task in Todo_j:
            if Task.get('userId') == int(uID):
                title = Task.get('title')
                name = reponse.get('username')
                tuid = Task.get('userId')
                status = Task.get('completed')
                writer.writerow(['{}'.format(tuid),
                                 '{}'.format(name),
                                 '{}'.format(status),
                                 '{}'.format(title)
                                 ])

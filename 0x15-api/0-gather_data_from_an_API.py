#!/usr/bin/python3
""" """
import requests
import sys

# Get request To This URL : https://jsonplaceholder.typicode.com/todos
# Parse the Json Reponse to Extract the Employer name from https://jsonplaceholder.typicode.com/users
# take the ID as argument
#  Print them in Certain Format (Name & Done_Tasks & Total Number of Tasks)
# Loop & print eh entire Completed Task Use 1 Tabulation & 1 Space

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    else:
        User_ID = sys.argv[1]
        ToDo_URL = "https://jsonplaceholder.typicode.com/todos"


        Todo_r = requests.get(ToDo_URL)
        Todo_j = Todo_r.json()
        for todo in Todo_j:
            title = todo.get('title')
            print("{}".format(title))
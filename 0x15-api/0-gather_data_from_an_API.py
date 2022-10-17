#!/usr/bin/python3
"""uses url https://jsonplaceholder.typicode.com/ 
    together with the user input(UserId)to get employees todo list
"""
from turtle import title
import requests
import urllib.request
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    

    user_tasks = []
    for task in todos:
        if task["userId"] == user["id"]:
            user_tasks.append(task)
    
    complete_tasks = []
    for task in user_tasks:
        if task['completed'] is True:
            complete_tasks.append(task)
    
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(complete_tasks), len(user_tasks)))

complete_title = [t.get('title')for t in todos if t.get('completed') is True]
[print("\t {}".format(title)) for title in complete_title]
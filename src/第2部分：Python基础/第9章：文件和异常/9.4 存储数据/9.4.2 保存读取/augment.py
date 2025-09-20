import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = 'username.json'
try:
    with open(filename) as file_obj:
        username = json.load(file_obj)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename) as file_obj:
        json.dump(username, filename)
        print("We will remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
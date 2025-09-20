import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_stored_username(filename: str) -> str:
    try:
        with open(filename) as file_obj:
            name = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return name

def get_new_username(filename: str):
    new_username = input("Please input a new name: ")
    try:
        with open(filename, 'w') as file_obj:
            json.dump(new_username, file_obj)
    except FileNotFoundError:
        print("There doesn't exist this file.")
    else:
        return new_username
    

def greet_user(filename: str):
    username = get_stored_username(filename)
    if username:
        print("welcome back, " + username + "!")
    else:
        username = get_new_username(filename)
        print("We will remember you when you come back, " + username + "!")
    
filename = 'username.json'
greet_user(filename)
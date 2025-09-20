import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

username = input("What is your name?")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We will remember you when you come back, " + username + "!")
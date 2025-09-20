import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
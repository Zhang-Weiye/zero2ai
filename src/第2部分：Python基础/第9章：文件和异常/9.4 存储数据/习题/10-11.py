import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def store_num(filename: str):
    num = input("Please input your favorite number ")
    try:
        with open(filename, 'w') as file_obj:
            json.dump(num, file_obj)
    except FileNotFoundError:
        print("This file doesn't exist.")
        
def read_num(filename: str):
    try:
        with open(filename, 'r') as file_obj:
            number = json.load(file_obj)
    except FileNotFoundError:
        print("This file doesn't exist.")
    else:
        print("I know your favorite number! It's " + number)
        
filename = '10-11.json'
store_num(filename)
read_num(filename)
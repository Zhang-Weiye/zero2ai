import os 
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def remember_num(filename: str):
    try:
        with open(filename) as file_obj:
            num = json.load(file_obj)
    except FileNotFoundError:
        print("There doesn't exist this file.")
        number = input("Please input your favorite number: ")
        with open(filename, 'w') as file_obj:
            json.dump(number, file_obj)
            print("Your favorite number has been saved.")
    except json.JSONDecodeError:
        print("The file exists but is empty or invalid. Let's fix it.")
        number = input("Please input your favorite number: ")
        with open(filename, 'w') as file_obj:
            json.dump(number, file_obj)
            print("Your favorite number has been saved.")
    else:
        if num:
            print("I know your favorite number! It's " + num)

filename = '10-12.json'
remember_num(filename)
            
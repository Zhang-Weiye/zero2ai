import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = "numbers.json"

with open(filename, 'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
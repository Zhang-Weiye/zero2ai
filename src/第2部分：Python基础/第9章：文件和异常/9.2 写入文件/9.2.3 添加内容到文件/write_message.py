import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_name = "programming.txt"
with open(file_name, 'a') as file_object:
    file_object.write("\nI also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
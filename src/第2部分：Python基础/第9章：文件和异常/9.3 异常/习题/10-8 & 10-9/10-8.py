import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def read_file(filename):
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        print(f"can't find the file {filename}")
    else:
        print(contents)
        
read_file('cats.txt')
read_file('dogs.txt')
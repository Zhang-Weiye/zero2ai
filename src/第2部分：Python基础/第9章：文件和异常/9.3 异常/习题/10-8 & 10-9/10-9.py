import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def read_file(filename):
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)
        
read_file('cats1.txt')
read_file('dogs1.txt')
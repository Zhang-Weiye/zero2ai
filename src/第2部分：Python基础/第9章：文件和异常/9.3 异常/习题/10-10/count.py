import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def count(filename, word):
    try:
        with open(filename, encoding='utf-8') as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        print("This file is not found.")
        return None
    else:
        return contents.count(word)
    
num_i = count('hamlet.txt', 'I')
print(num_i)

num_dream = count('hamlet.txt', 'dream')
print(num_dream)
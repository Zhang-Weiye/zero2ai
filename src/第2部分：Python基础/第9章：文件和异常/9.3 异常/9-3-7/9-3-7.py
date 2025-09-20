import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        print("This file doesn't exist!")
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
        

count_words('alice.txt')
count_words('hamlet.txt')
count_words('wizard.txt')
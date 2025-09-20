import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = 'pi_million_digits.txt'
with open(filename) as file:
    lines = file.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

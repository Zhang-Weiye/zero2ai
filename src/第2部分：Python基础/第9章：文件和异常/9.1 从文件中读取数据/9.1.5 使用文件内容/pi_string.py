import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('pi.txt') as f:
    lines = f.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))
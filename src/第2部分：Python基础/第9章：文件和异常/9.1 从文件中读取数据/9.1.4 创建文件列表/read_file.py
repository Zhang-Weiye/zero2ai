import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('pi.txt') as file:
    lines = file.readlines()
    
for line in lines:
    print(line.rstrip())
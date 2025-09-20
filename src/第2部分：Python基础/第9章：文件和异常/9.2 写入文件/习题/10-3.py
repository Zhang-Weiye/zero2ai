import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("guest.txt", 'a') as file_obj:
    file_obj.write("\n")
    file_obj.write(input("Please input your name: "))

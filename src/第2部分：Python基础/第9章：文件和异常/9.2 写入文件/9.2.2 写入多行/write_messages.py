import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("without_newline.txt", 'w') as file_obj:
    file_obj.write("I love programming.")
    file_obj.write("I love python")
    
with open("with_newline.txt", 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love python.\n")
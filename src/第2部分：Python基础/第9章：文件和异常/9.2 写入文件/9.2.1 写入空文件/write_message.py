import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename = 'programming.txt'
# 即使这个文件夹不存在，也会新建一个文件夹出来
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
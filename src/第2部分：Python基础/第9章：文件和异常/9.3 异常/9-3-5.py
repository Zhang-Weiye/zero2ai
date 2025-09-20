import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 错误示例
# file_name = 'alice.txt'
# with open(file_name) as f_obj:
#     contents = f_obj.read()

#  正确做法
file_name = 'alice.txt'
try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + "doesn't exist."
    print(msg)
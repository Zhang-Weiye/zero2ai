import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

# 使用相对路径打开
with open('text_files/filename.txt') as f:
    print(f.read())
    
    
# 使用绝对路径打开
with open('F:/zero2ai/src/第2部分：Python基础/第9章：文件和异常/9.1 从文件中读取数据/9.1.2 文件路径/text_files/filename.txt') as f:
    print(f.read())
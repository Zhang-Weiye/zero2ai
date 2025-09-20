import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('pi.txt') as f:
    for line in f:
        print(line)
        
        
# 在文件中，每行的末尾都有一个看不见的换行符
# print()是也会将换行符打印出来，若要消除需要使用rstrip()
print("\n")
with open('pi.txt') as f:
    for line in f:
        print(line.rstrip())
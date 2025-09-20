import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

numbers = [2, 3, 5, 7, 11, 13]

filename = "numbers.json"
with open(filename, 'w') as file_obj:
    # json.dump()接受两个参数，要存储的数据以及可用于存储数据的文件对象
    json.dump(numbers, file_obj)
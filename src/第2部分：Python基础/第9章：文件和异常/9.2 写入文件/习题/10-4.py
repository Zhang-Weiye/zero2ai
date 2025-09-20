import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

signal = input("Please input your name(Enter q to quit): ")
with open('guest_book.txt', 'a') as file_obj:
    while signal != 'q':
        file_obj.write(signal + "\n")
        print(f"Hi, welcome here {signal} !")
        signal = input("Please input your name(Enter q to quit): ")
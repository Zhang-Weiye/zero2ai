import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('10-5.txt', 'a') as file_obj:
        while True:
            reason = input("Please Enter your reason for loving programming (q to quit) : ")
            if reason.rstrip().lower() == 'q':
                break
            else:
                file_obj.write(reason)

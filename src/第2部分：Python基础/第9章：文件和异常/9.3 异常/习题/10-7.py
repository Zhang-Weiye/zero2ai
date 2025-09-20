print("Please input two numbers for add computation.\n")


while True:
    try:
        first = input("Please input the first number: ")
        num_first = int(first)
    except ValueError:
        print("Your input is not a number!")
        continue
    else:
        break
    

while True:
    try:
        second = input("Please input the second number: ")
        num_second = int(second)
    except ValueError:
        print("Your input is not a number!")
        continue
    else:
        break
    
sum = num_first + num_second
print(f"The sum is {sum}.")
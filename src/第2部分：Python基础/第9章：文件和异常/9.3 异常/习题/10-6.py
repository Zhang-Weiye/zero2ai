print("Please input two numbers for add calculation.")

def get_num(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please input a number.")
        
first = get_num("Please input the first number:")
second = get_num("Please input the second number:")

try:
    total = first + second
except TypeError:
    print("unsupported computation")
else:
    print(f"The sum is {total}.")

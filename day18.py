

print("===== CALCULATOR PRO =====\n")
def get_two_numbers():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return x, y
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b
def mod(a,b):
    return a % b
def pow(a,b):
    return a ** b
def square(a):
    return a**2
def cube(a):
    return a**3


while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5.Modulus")
    print("6.Power")
    print("7. Square")
    print("8. Cube")
    print("9. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 9:
        print("Thank u for using Calculator Pro!")
        break
    elif ch == 1:
        x, y = get_two_numbers()
        print(f"Addition of {x} & {y} = {add(x,y)}")
    elif ch == 2:
        x,y = get_two_numbers()
        print(f"Subtraction of {y} from {x} = {sub(x,y)}")
    elif ch == 3:
        x,y = get_two_numbers()
        print(f"Multiplication of {x} & {y} = {mul(x,y)}")

    elif ch == 4:
        x,y = get_two_numbers()
        print(f"Division of {x} & {y} = {div(x,y)}")
    
    elif ch == 5:
        x,y = get_two_numbers()
        print(f"Modulo of {x} & {y} = {mod(x,y)}")

    elif ch == 6:
        x,y = get_two_numbers()
        print(f"{x} raised to {y} = {pow(x,y)}")


    elif ch == 7:
        x = int(input("Enter the number:"))
        print(f"Square of {x} = {square(x)}")

    elif ch == 8:
        x = int(input("Enter the number:"))
        print(f"Cube of {x} = {cube(x)}")

    else:
        print("Invalid Input!")
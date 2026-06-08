import calculator
while True:
    ch = int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit\n"))
    if ch == 5:
        break
    num1 = int(input("enter the 1st num:"))
    num2 = int(input("enter the 2nd num:"))
    if ch == 2:
        print(calculator.sub(num1,num2))
    elif ch == 3:
        print(calculator.mul(num1,num2))
    elif ch == 4:
        print(calculator.div(num1,num2))
    elif ch == 1:
        print(calculator.add(num1,num2))
    else:
        print("Invalid Input")

    
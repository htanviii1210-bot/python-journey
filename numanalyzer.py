


print("Welcome To Even Odd App!")
nums = list(map(int, input("Enter numbers by seperating spaces:").split()))
even = [num for num in nums if num % 2 == 0]
odd = [num for num in nums if num % 2!= 0]
pos = [num for num in nums if num > 0]
neg = [num for num in nums if num < 0]
sq = [num*num for num in nums]
cube = [num**3 for num in nums]
greaterthan5 = [num for num in nums if num > 5]
while True:
    print("\n1.Even\n2.Odd\n3.Positive\n4.Negative\n5.Squares\n6.Cubes\n7.Greater Than 5\n8.All\n9.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 9:
        print("Thank u for using the NumAnalyzer!")
        break
    elif ch == 1:
        print(f"Even : {even}")
    elif ch == 2:
        print(f"Odd : {odd}")
    elif ch == 3:
        print(f"Positive : {pos}")
    elif ch == 4:
        print(f"Negative : {neg}")
    elif ch == 5:
        print(f"Squares = {sq}")
    elif ch == 6:
        print(f"Cubes : {cube}")
    elif ch == 7:
        print(f"Greater than 5 : {greaterthan5}")
    elif ch == 8:
        print(f"Even : {even}")
        print(f"Odd : {odd}")
        print(f"Positive : {pos}")
        print(f"Negative : {neg}")
        print(f"Squares = {sq}")
        print(f"Cubes : {cube}")
        print(f"Greater than 5 : {greaterthan5}")
    else:
        print("Invalid Input!")
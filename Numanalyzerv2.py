
print("Welcome To Functional Number Analyzer!\n")
nums = list(map(int,input("Enter numbers seperated by spaces:").split()))
squares = list(map(lambda x: x*x, nums))
cubes = list(map(lambda x:x**3,nums))
evens = list(filter(lambda x:x%2 == 0,nums))
odds = list(filter(lambda x:x%2!=0 ,nums))
greaterthan = list(filter(lambda x:x > 15,nums))
while True:
    print("1. Show Squares\n2. Show Cubes\n3. Show Even Numbers\n4. Show Odd Numbers\n5. Show Numbers Greater Than 15\n6. Show All\n7. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 7:
        print("Thank u for using the Functional Number Analyzer!")
        break
    elif ch == 1:
        print(f"Squares : \n{squares}")
    elif ch == 2:
        print(f"Cubes : \n{cubes}")
    elif ch == 3:
        print(f"Even numbers : \n{evens}")
    elif ch == 4:
        print(f"Odd numbers : \n{odds}")
    elif ch == 5:
        print(f"Greater Than 15 : \n{greaterthan}")
    elif ch == 6:
        print(f"Squares : \n{squares}")
        print(f"Cubes : \n{cubes}")
        print(f"Even numbers : \n{evens}")
        print(f"Odd numbers : \n{odds}")
        print(f"Greater Than 15 : \n{greaterthan}")
    else:
        print("Invalid Input!")
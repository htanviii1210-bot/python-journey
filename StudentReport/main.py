from grade_utils import *
marks = list(map(int,input("Enter the marks of the student:").split()))
while True:
    print("1. Passed Students")
    print("2. Failed Students")
    print("3. Distinction Students")
    print("4. Average")
    print("5. Highest")
    print("6. Lowest")
    print("7. Show All")
    print("8. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 8:
        print("Thank u for using this app!")
        break
    elif ch == 1:
        print(f"Passed Students : {passed_students(marks)}")
    elif ch == 2:
        print(f"Failed Students : {failed_students(marks)}")
    elif ch == 3:
        print(f"Distinction Students : {distinction_students(marks)}")
    elif ch == 4:
        print(f"Average : {average(marks)}")
    elif ch == 5:
        print(f"Highest : {highest(marks)}")
    elif ch == 6:
        print(f"Lowest : {lowest(marks)}")
    elif ch == 7:
        print(f"Passed Students : {passed_students(marks)}")
        print(f"Failed Students : {failed_students(marks)}")
        print(f"Distinction Students : {distinction_students(marks)}")
        print(f"Average : {average(marks)}")
        print(f"Highest : {highest(marks)}")
        print(f"Lowest : {lowest(marks)}")
    else:
        print("Invalid Input!")
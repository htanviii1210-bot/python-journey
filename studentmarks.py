

print("Welcome to The Student Marks Analyzer:")
marks = list(map(int,input("Enter the marks of the students with spaces:").split()))
passed = [mark for mark in marks if mark >= 40]
failed = [mark for mark in marks if mark < 40]
distinction = [mark for mark in marks if mark >= 75]
avg = round(sum(marks)/len(marks), 2)
highest = max(marks)
lowest = min(marks)
while True:
    print("\n1. Passed Students\n2. Failed Students\n3. Distinction Students\n4. Average Marks\n5. Highest Marks\n6. Lowest Marks\n7. All Statistics\n8. Exit")
    ch = int(input("Enter the choice:"))
    if ch == 8:
        print("Thank u for using The marks Analyzer!")
        break
    elif ch == 1:
        print(f"Passed Students : {passed}")
    elif ch == 2:
        print(f"Failed Students : {failed}")
    elif ch == 3:
        print(f"Distinction : {distinction}")
    elif ch == 4:
        print(f"Average Marks: {avg}")
    elif ch == 5:
        print(f"Highest Marks : {highest}")
    elif ch == 6:
        print(f"Lowest Marks : {lowest}")
    elif ch == 7:
        print(f"Passed Students : {passed}")
        print(f"Failed Students : {failed}")
        print(f"Distinction : {distinction}")
        print("\n")
        print(f"Average Marks: {avg}")
        print(f"Highest Marks : {highest}")
        print(f"Lowest Marks : {lowest}")
    else:
        print("Invalid Input!")
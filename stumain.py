import json
print("Welcome To Student Record System!")
try:
    with open("students.json","r") as file:
        students = json.load(file)
except:
    students = []
while True:
    print("\n1.Add Student info")
    print("\n2.View All")
    print("\n3.Total Number of Students")
    print("\n4.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 4:
        print("Thank u for using the Student Record System!")
        break
    elif ch == 1:
        name = input("Enter name of The Student:")
        marks = int(input("Enter marks:"))

        student = {
            "name" : name,
            "marks" : marks,
        }
        students.append(student)

        with open("students.json","w") as file:
            json.dump(students,file)
        print("Student info has been Added Successfully!")
    elif ch == 2:
        for s in students:
            print(f"Name: {s['name']} , Marks: {s['marks']}")
    elif ch == 3:
        print(f"Total no. of students={len(students)}")
    else:
        print("invalid input")



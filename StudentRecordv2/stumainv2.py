import json
print("Welcome To The Student Record System v2!")

try:
    with open("studentsv2.json","r") as file:
        studentsv2 = json.load(file)
except:
    studentsv2 = []

while True:
    print("\n1.Add Student info")
    print("\n2.View All")
    print("\n3.Total Number of Students")
    print("\n4.Exit")
    try:
        ch = int(input("Enter a number:"))
    except ValueError:
        print("Pls enter a number!")
        continue
    if ch == 4:
        print("Thank u for using The Student Record System v2!")
        break
    elif ch == 1:
        name = input("Enter Student's name:")
        while True:
            try:
                marks = int(input("Enter marks of the student:"))
                break
            except ValueError:
                print("Enter a number!")
        while True:
            try:
                age = int(input("Enter age of the student :"))
                break
            except ValueError:
                print("Enter a number !")
        student = {
            "name" : name,
            "marks" : marks,
            "age" : age
        }
        studentsv2.append(student)
        with open("studentsv2.json","w") as file:
            json.dump(studentsv2,file)
        print("Data added succesfully!")
    elif ch == 2:
        for s in studentsv2:
            print(f"Name: {s['name']} , Marks: {s['marks']} , Age: {s['age']}")
    elif ch == 3:
        print(f"Total no. of students={len(studentsv2)}")
    else:
        print("invalid input")


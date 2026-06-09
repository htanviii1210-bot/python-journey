import json

with open("student.json","r") as file:
    student = json.load(file)


name = input("Enter students name:")
age = int(input("Enter students age:"))
marks = int(input("Enter students marks:"))

students = {
    "name" : "T",
    "age" : 18,
    "marks" : 100
}

student.append(students)

with open("student.json","w") as file:
    json.dump(student,file,indent=4)
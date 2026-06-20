import json

print("Welcome To Learning Tracker!")
try:
    with open("days.json","r") as file:
        days = json.load(file)
except:
    days = []

while True:
    print("\n1. Add Today's Entry")
    print("\n2. View All Entries")
    print("\n3. Search by Date")
    print("\n4. Count Total Entries")
    print("\n5. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 5:
        print("Thank u for using the Learning Tracker!")
        break
    elif ch == 1:
        day = int(input("Enter the day number:"))
        topic = input("Enter the topic learnt:")
        project = input("Enter the project built:")
        student = {
            "day" : day,
            "topic" : topic,
            "project" : project
        }
        days.append(student)

        with open("days.json","w") as file:
            json.dump(days,file)
        print("Info has been added successfully!")
    elif ch == 2:
        for d in days:
            print(f"Day:{d['day']} , Topic:{d['topic']} , Project:{d['project']}")
    elif ch == 3:
        daynum = int(input("Enter the day u want to search for:"))
        flag = False
        for d in days:
            if d['day'] == daynum:
                print(f"Day:{d['day']} , Topic: {d['topic']}, Project: {d['project']}")
                flag = True
            if flag == False:
                print("Not Found")
    elif ch == 4:
        print(f"Total entries={len(days)}")
    else:
        print("Invalid Input!")
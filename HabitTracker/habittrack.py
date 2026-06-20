import json
import os

print(os.path.abspath("habit.json"))
try:
    with open("habit.json","r") as file:
        habit = json.load(file)
except:
    habit = []

while True:
    print("\n1. Add Habit\n2. View All Habits\n3. Search Habit\n4. Total Habits\n5. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 5:
        print("Thank u for using the habit tracker!")
        break
    elif ch == 1:
        name = input("Enter ur habit:")
        streak = int(input("Enter the streak:"))
        habits = {
            "name" : name,
            "streak" : streak,
        }
        habit.append(habits)
        with open("habit.json","w") as file:
            json.dump(habit,file)
        print("Info has been added successfully!")
    elif ch == 2:
        for h in habit:
            print(f"Habit: {h['name']}, Streak: {h['streak']}")
    elif ch == 3:
        habitname = input("Enter the habit name:")
        flag = False
        for h in habit:
            if habitname == h['name']:
                print(f"Habit: {h['name']}, Streak: {h['streak']}")
                flag = True
        if flag == False:
            print("Not Found!")
    elif ch == 4:
        print(f"Total entries = {len(habit)}")
    else:
        print("Invalid Input!")

        
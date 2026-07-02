days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


steps = list(map(int ,input("Enter ur step count evry day of the week from Monday to Sunday:").split()))
daysabove = list(filter(lambda x:x > 10000,steps))
daysbelow = list(filter(lambda x:x < 5000,steps))
total = sum(steps)
avg = total//len(steps)
improve = list(map(lambda x: int(x * 1.1), steps))
best = days[steps.index(max(steps))]
worst = days[steps.index(min(steps))]

while True:
    print("1. Days above 10000 steps")
    print("2. Days below 5000 steps")
    print("3. Total weekly steps")
    print("4. Average daily steps")
    print("5. Add a 10 percent improvement challenge")
    print("6. Best day")
    print("7. Worst day")
    print("8. Show all statistics")
    print("9. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 9:
        print("Thank u for using the Fitness Tracker!:)")
        break
    elif ch == 1:
        print(f"Days above 10000 steps : \n{daysabove}")
    elif ch == 2:
        print(f"Days below 5000 steps : \n{daysbelow}")
    elif ch == 3:
        print(f"Total weekly steps : \n{total}")
    elif ch == 4:
        print(f"Average daily steps : \n{avg}")
    elif ch == 5:
        print(f"Next weeks Challenge : \n{improve}")
    elif ch == 6:
        print(f"Best Day : \n{best}")
    elif ch == 7:
        print(f"Worst Day : \n{worst}")
    elif ch == 8:
        print("All Statistics :\n")
        print(f"Days above 10000 steps : \n{daysabove}")
        print(f"Days below 5000 steps : \n{daysbelow}")
        print(f"Total weekly steps : \n{total}")
        print(f"Average daily steps : \n{avg}")
        print(f"Next weeks Challenge : \n{improve}")
        print(f"Best Day : \n{best}")
        print(f"Worst Day : \n{worst}")
    else:
        print("Invalid Input!:(")
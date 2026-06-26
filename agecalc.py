from datetime import datetime

print("Welcome To The Age Calculator!")

while True:
    print("\n1.To calculate ur age \n2.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 2:
        print("Thank u for using this app!")
        break
    elif ch == 1:
        birthday = int(input("Enter your birth day:"))
        birthmonth = int(input("Enter your birth month:"))
        birthyear = int(input("Enter your birth year:"))

        now = datetime.now()
        days = now.day - birthday
        if now.month < birthmonth:
            month = (now.month - birthmonth) + 12 
        elif now.month > birthmonth:
            month = (birthmonth - now.month) + 12 
        else:
            month = 0
        if 0 < month < 12:
            age = (now.year - birthyear) -1
        else:
            age = now.year - birthyear
        if month == 0 and days == 0:
            print("Happy Birthday!")
        print(f"Your age is {age} years {month} months {days} days!")
    else:
        print("Invalid input!")
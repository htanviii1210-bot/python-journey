#Add expense
#View expense
#Show total spending
expenses = []
print("Welcome To The Expense Tracker!")
total = 0
while True:
    print("\n1.Add Expense")
    print("\n2.View Expense")
    print("\n3.Show Total Expense")
    print("\n4.Exit")
    ch = int(input("Enter ur choice:"))
    if ch==4:
        print("Thank u for using Expense Tracker!")
        break
    elif ch == 1:
        title = input("Enter the title of the expense:")
        category = input("Enter the category:")
        amt = int(input("Enter the amount:")) 
        expense = {
            "title" : title,
            "category" : category,
            "amt" : amt,
        }
        total = total+amt
        expenses.append(expense)
    elif ch == 2:
        print(expenses)
    elif ch == 3:
        print(total)
    else:
        print("Invalid Input")

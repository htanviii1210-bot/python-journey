

expenses = list(map(int ,input("Enter ur expenses seperated by spaces:\n").split()))
expensesabove = list(filter(lambda x:x > 500, expenses))
expensesbelow = list(filter(lambda x:x < 500, expenses))
highestexp = max(expenses)
lowestexp = min(expenses)
total = sum(expenses)
avg = round(total/len(expenses), 2)
gstadded = list(map(lambda x:round(x * 1.18, 2), expenses))
discount = list(map(lambda x:round(x * 0.9, 2), expenses))
while True:
    print("1. Show all expenses")
    print("2. Expenses above ₹500")
    print("3. Expenses below ₹500")
    print("4. Highest expense")
    print("5. Lowest expense")
    print("6. Total spending")
    print("7. Average spending")
    print("8. Show expenses with 18 percent GST added")
    print("9. Show expenses after 10 percent discount")
    print("10. Show all statistics")
    print("11. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 11:
        print("Thank u for using Expense Tracker v2!")
        break
    elif ch == 1:
        print(f"Your Expenses are : \n{expenses}")
    elif ch == 2:
        print(f"Expenses above 500 : \n{expensesabove}")
    elif ch == 3:
        print(f"Expenses below 500 : \n{expensesbelow}")
    elif ch == 4:
        print(f"Highest Expense : \n{highestexp}")
    elif ch == 5:
        print(f"Lowest Expense : \n{lowestexp}")
    elif ch == 6:
        print(f"Total Spending : \n{total}")
    elif ch == 7:
        print(f"Average Spending : \n{avg}")
    elif ch == 8:
        print(f"Expenses with 18 percent GST added : \n{gstadded}")
    elif ch == 9:
        print(f"Expenses after 10 percent discount : \n{discount}")
    elif ch == 10:
        print(f"All statistics : \n")
        print(f"Your Expenses are : \n{expenses}")
        print(f"Expenses above 500 : \n{expensesabove}")
        print(f"Expenses below 500 : \n{expensesbelow}")
        print(f"Highest Expense : \n{highestexp}")
        print(f"Lowest Expense : \n{lowestexp}")
        print(f"Total Spending : \n{total}")
        print(f"Average Spending : \n{avg}")
        print(f"Expenses with 18 percent GST added : \n{gstadded}")
        print(f"Expenses after 10 percent discount : \n{discount}")
    else:
        print("Invalid Input!")
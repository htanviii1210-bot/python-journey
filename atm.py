balance = 5000
while True:
    print("\n1.Check Balance")
    print("\n2.Deposit Money")
    print("\n3.Withdraw Money")
    print("\n4.Exit")

    ch=input("Enter the number:")

    if ch == "4":
        print("Thank u for using the ATM!")
        break
    elif ch == "2":
        amt = int(input("Enter the amount u want to deposit:"))
        balance+=amt
    elif ch == "3":
        amt = int(input("Enter the amount u want to withdraw:"))
        if amt <= balance:
            balance= balance-amt
            print(f"Your current balance is {balance}")
        else:
            print("Insufficient Balance")
    elif ch =="1":
        print(f"Your current balance is {balance}")
    else:
        print("Invalid Input")
        

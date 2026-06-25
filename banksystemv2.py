print("Welcome to Bank System v2!")

class BankAcc:
    def __init__(self,owner,bal,accnum):
        self.owner = owner
        self.bal = bal
        self.accnum = accnum
        self.transactions = []
        print(f"\nWelcome {self.owner}!")
    
    def deposit(self,amt):
        if amt <= 0:
            print("Invalid amount")
        else:
            self.bal += amt
            self.transactions.append(f"Deposited ₹{amt}")
            print(f"₹{amt} deposited successfully!")

    def withdraw(self,amt):
        if amt <= 0:
            print("Invalid amount")
        elif amt > self.bal:
            print("Insufficient Funds!")
        else:
            self.bal -= amt
            self.transactions.append(f"Withdrawn ₹{amt}")
            print(f"₹{amt} withdrawn successfully!")
    
    def display_bal(self):
        print(f"Current Balance: ₹{self.bal}")

    def showtransactions(self):
        if len(self.transactions) == 0:
            print("No transaction history")
        else:
            for transaction in self.transactions:
                print(transaction)
owner = input("Enter account holder's name:")
bal = float(input("Enter the initial balance in the account:"))
accnum = (input("Enter your account number:"))

acc = BankAcc(owner,bal,accnum)
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Show all transactions and history")
    print("5. Exit")

    ch = int(input("Enter your choice:"))

    if ch == 5:
        print("Thanks for using Bank Account System v2!")
        break
    elif ch == 1:
        amt = float(input("Enter the amount to be deposited:"))
        acc.deposit(amt)
    elif ch == 2:
        amt = float(input("Enter the amount to be withdrawn:"))
        acc.withdraw(amt)
    elif ch == 3:
        acc.display_bal()
    elif ch == 4:
        acc.showtransactions()
    else:
        print("Invalid choice! Please try again.")
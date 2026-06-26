print("Welcome to Bank System v2!")

class BankAcc:
    def __init__(self, owner, bal, accnum):
        self.owner = owner
        self.bal = bal
        self.accnum = accnum
        self.transactions = []

    def deposit(self, amt):
        self.bal += amt
        self.transactions.append(f"Deposited ₹{amt}")

    def withdraw(self, amt):
        if amt > self.bal:
            print("Insufficient funds!")
        else:
            self.bal -= amt
            self.transactions.append(f"Withdrawn ₹{amt}")

    def display_balance(self):
        print(f"Current Balance: ₹{self.bal}")

    def show_transactions(self):
        if len(self.transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)


owner = input("Enter name: ")
bal = float(input("Enter balance: "))
accnum = input("Enter account number: ")

acc = BankAcc(owner, bal, accnum)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Show Transactions")
    print("5. Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        amt = float(input("Amount: "))
        acc.deposit(amt)

    elif ch == 2:
        amt = float(input("Amount: "))
        acc.withdraw(amt)

    elif ch == 3:
        acc.display_balance()

    elif ch == 4:
        acc.show_transactions()

    elif ch == 5:
        break

    else:
        print("Invalid choice")
print("Welcome To The Bank Account System!")

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"\nWelcome, {self.owner}!")

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")


owner = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(owner, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank you for using the Bank Account System!")
        break

    else:
        print("Invalid choice! Please try again.")
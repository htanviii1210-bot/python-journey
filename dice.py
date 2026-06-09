import random

print("Welcome to roll a die:")
def roll():
    num = random.randint(1,6)
    print(f"The number rolled is {num}")

while True:
    ch = input("Want To Roll The Dice?(y/n):")
    if ch=="y" or ch=="Y":
        roll()
    elif ch=="n" or ch=="N":
        break
    else:
        print("Invalid Input!")


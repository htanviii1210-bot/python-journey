import random
choices = ["Rock", "Paper", "Scissors"]
print("Welcome to the rock paper scissor game!")
print("Enter 0 for rock, 1 for paper and 2 for scissor!")
ch=int(input("Enter your choice:"))
if 0 <= ch <len(choices):
    compch=random.randint(0,2)
    print(f"Computer chose {choices[compch]}")
    print(f"U chose {choices[ch]}")
    if (ch==0 and compch==1) or (ch==1 and compch==2) or (ch==2 and compch==0):
        print("You lose")
    elif (ch==0 and compch==2) or (ch==1 and compch==0) or (ch==2 and compch==1):
        print("You win")
    elif (ch==0 and compch==0) or (ch==1 and compch==1) or(ch==2 and compch==2):
        print("Its a draw!")
else:
    print("Invalid input!")

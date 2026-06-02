import random
print("Welcome to the number guessing game!")
print("You have to guess a random number in range 1 and 10")

mode=str(input("Enter the mode of difficulty if easy then ull get 10 guesses if hard then 5 guesses"))
num=random.randint(1,10)
won = False
if mode=="easy":
    for i in range(10):
        n=int(input("Enter the guess:"))
        if n==num:
            print(f"Correct Guess You win at attempt {i+1}")
            won=True
            break
        else:
            if n<num:
                print("Wrong Guess Too Low!")
            elif n>num:
                print("Wrong Guess Too High!")
            

elif mode=="hard":
    for i in range(5):
        n=int(input("Enter the guess:"))
        if n==num:
            print(f"Correct Guess You win at attempt {i+1}")
            won=True
            break
        else:
            if n<num:
                print("Wrong Guess Too Low!")
            elif n>num:
                print("Wrong Guess Too High!")
else:
    print("Invalid Input!")

if not won:
    print(f"Game Over The number was {num}")

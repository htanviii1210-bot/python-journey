score = 0
a=1

quiz = {
    "Capital of France?": "Paris",
    "2+2?": "4",
    "Largest planet?": "Jupiter",
}
print("Welcome to the quiz Game:")
for i in quiz:
    print(f"Question {a}/{len(quiz)}")
    print(i)
    ans=str(input("Your Answer:"))
    a+=1
    if ans==quiz[i]:
        score=score+1
        print(f"Correct Answer your current score is {score}")
    else:
        print(f"Wrong Answer the Correct Answer is {quiz[i]}")

print(f"Your Final Score is {score}")
percentage=(score/len(quiz))*100
print(f"Your percentage is {percentage}%")
print("Welcome to the expense tracker")
bud=int(input("Enter ur monthly budget:"))
total=0
highest=0
n=int(input("How many expenses do u want to enter:"))
for i in range(n):
    exp=int(input(f"Enter expense{i+1}:"))
    total=total+exp
    if(highest<exp):
       highest=exp
if(total>bud):
    rem=total-bud
    
    print(f"ur exceeded budget is {rem}")
else:
    rem=bud-total
    print(f"ur remaining budget is {rem}")
       
print(f"Your expense total is={total}")
avg=total/n
print(f"Your average is {avg}")
print(f"The highest expense has been {highest}")

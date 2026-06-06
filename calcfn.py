def add(n1,n2):
    result = n1+n2
    return result
def sub(n1,n2):
    result = n1-n2
    return result
    
def mul(n1,n2):
    result = n1*n2
    return result
    
def div(n1,n2):
    if n1==0 or n2==0:
        result = 0
    else:
        result = n1/n2
    
    return result

print("\n1.Add")
print("\n2.Subtract")
print("\n3.Multiply")
print("\n4.Divide")
print("\n5.Exit")

ch = input("Enter the number of the operation:")

if ch =="1":
    num1 = int(input("Enter the first no.:"))
    num2 = int(input("Enter the second no.:"))
    add(num1,num2)
elif ch =="2":
    num1 = int(input("Enter the first no.:"))
    num2 = int(input("Enter the second no.:"))
    sub(num1,num2)
elif ch=="3":
    num1 = int(input("Enter the first no.:"))
    num2 = int(input("Enter the second no.:"))
    mul(num1,num2)
elif ch=="4":
    num1 = int(input("Enter the first no.:"))
    num2 = int(input("Enter the second no.:"))
    div(num1,num2)
elif ch=="5":
    exit
else:
    print("Invalid Input")
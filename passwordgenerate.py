import random
letters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

numbers = [
    "0","1","2","3","4","5","6","7","8","9"
]

symbols = [
    "!","@","#","$","%","^","&","*","(",")",
    "-","_","=","+","[","]","{","}","|","\\",
    ";",":","'","\"",",",".","<",">","/","?"
]

numlet=int(input("Enter the number of letters:"))
numnum=int(input("Enter the number of digits:"))
numsym=int(input("Enter the number of symbols:"))


pw=[]
for char in range(numlet):
    pw.append(random.choice(letters))
for char in range(numnum):
    pw.append(random.choice(numbers))
for char in range(numsym):
    pw.append(random.choice(symbols))
random.shuffle(pw)
finalpw="".join(pw)
print(finalpw)

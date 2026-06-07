print("Welcome to the notes app")
while True:
    ch=input("\n1.Add Entry\n2.View Entries\n3.exit:")
    if ch == "1":
      note = input("Write a note:")
      file = open("journal.txt", "a")
      file.write(note+"\n")
      file.close() 
    elif ch == "2":
       file = open("journal.txt", "r")
       data = file.read()
       print(data)
       file.close()
    elif ch == "3":
       break
    else:
       print("Invalid Input")
       


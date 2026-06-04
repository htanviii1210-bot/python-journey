tasks = [
    "Learn Python functions",
    "Push code to GitHub",
    "Solve 2 LeetCode problems",
    "Update README",
    "Watch Firebase tutorial",
    "Finish college assignment",
    "Revise loops and lists",
    "Build To-Do List project",
    "Exercise for 30 minutes",
    "Read 10 pages of a book"
]


while True:
    print("\n1.Add Task")
    print("\n2.View Task")
    print("\n3.Delete Task")
    print("\n4.Exit")


    choice=input("Enter ur choice:")
    if choice=="4":
        print("Thanks for using the To-Do List App!")
        break
    elif choice=="1":
        task1=input("Enter the task:")
        tasks.append(task1)
        print("Task added\n")
        for i, task in enumerate(tasks,start=1):
            print(f"{i}. {task}")
    elif choice=="2":
        if not tasks:
            print("No tasks available")
        else:
            for i, task in enumerate(tasks,start=1):
                print(f"{i}. {task}")
    elif choice=="3":
        if not tasks:
            print("No tasks left to be deleted!")
        else:
            print("Current List")
            for i, task in enumerate(tasks,start=1):
                print(f"{i}. {task}")
            ch=int(input("Enter the task number:"))
            ch=ch-1
            if 0 <= ch < len(tasks):
                tasks.pop(ch)
                print("Task deleted successfully!")
                for i, task in enumerate(tasks,start=1):
                    print(f"{i}. {task}")
            else:
                print("Invalid input!")
        
      
    else:
         print("Invalid choice")

    



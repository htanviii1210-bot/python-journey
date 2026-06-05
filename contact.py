contacts = {
    "Tanvi": "9876543210",
    "Rahul": "9123456789",
    "Priya": "9988776655",
    "Aman": "9999999999",
    "Neha": "9012345678"
}

while True:
    print("\n1.Add Contact")
    print("\n2.Search Contact")
    print("\n3.View Contact")
    print("\n4.Delete Contact")
    print("\n5.View All Contacts")
    print("\n6.Exit")

    ch=input("Enter ur choice:")
    if ch=="1":
        name=str(input("Enter the contacts name:"))
        phone=input("Enter the contacts phone no.:")
        
        if (name in contacts) or (phone in contacts.values()):
            print("This contact already exists")
        else:
            contacts[name] = phone
            print("Contact Added successfully!")

    elif ch=="2":
        name=str(input("Enter the contacts name:"))
        if name in contacts:
            print("Contact Found")
        else:
            print("Contact Not Found")
    elif ch=="3":
        name=str(input("Enter the contacts name that needs to be viewed:"))
        if name in contacts:
            print("Contact Found")
            print(contacts[name])
        else:
            print("Contact Not Found")
    elif ch=="4":
        name=str(input("Enter the contacts name that needs to be deleted:"))
        if name in contacts:
            contacts.pop(name)
            print("Contact Deleted Successfully")
        else:
            print("Contact Not Found")
    elif ch=="5":
        for name, ph in contacts.items():
            print(name,"-",ph)
    elif ch=="6":
        print("Thanks for using the contacts App")
        break
    else:
        print("Invalid Input")

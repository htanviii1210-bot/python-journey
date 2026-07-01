#1. Add Book
#2. View Books
#3. Search Book
#4. Delete Book
#5. Show Total Books
#6. Exit
import json
import os
print("Welcome To Library App v2!")
print(os.path.abspath("book.json"))
try:
    with open("book.json","r") as file:
        book = json.load(file)
except:
    book = []

while True:
    print("1. Add Book\n2. View Books\n3. Search Book\n4. Delete Book\n5. Show Total Books\n6. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 6:
        print("Thank u for using the Library v2 App!")
        break
    elif ch == 1:
        title = input("Enter the name of the book:")
        author = input("Enter the name of the author:")
        genre = input("Enter the genre:")
        year = int(input("Enter the year:"))
        books = {
            "title" : title,
            "author" : author,
            "genre" : genre,
            "year" : year,
        }
        book.append(books)
        with open("book.json","w") as file:
            json.dump(book,file)
            print(book)
        print("Info is added successfully!")
    elif ch == 2:
        for b in book:
            print(f"Title : {b['title']}\nAuthor : {b['author']}\nGenre : {b['genre']}\nYear : {b['year']}")
    elif ch == 3:
        bookname = input("Enter the name of the book:")
        flag = False
        for b in book:
            if bookname.lower() == b['title'].lower():
                print(f"Title : {b['title']}\nAuthor : {b['author']}\nGenre : {b['genre']}\nYear : {b['year']}")
                flag = True
        if flag == False:
            print("Not found:(")
    elif ch == 4:
        bookname = input("Enter book name to delete: ")
        for i in range(len(book)):
            if book[i]["title"].lower() == bookname.lower():
                book.pop(i)
                with open("book.json","w") as file:
                    json.dump(book,file, indent=4)
                print("Book has been deleted successfully!")
                break
    elif ch == 5:
        print(f"Number of books : {len(book)}")
    else:
        print("Invalid Input!")

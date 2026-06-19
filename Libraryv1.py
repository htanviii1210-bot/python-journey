#Add Book
#View All
#Search by genre
#total books
print("Welcome to Library Management App!")
books = []
total = 0
while True:
    print("\n1.Add Book")
    print("\n2.View All")
    print("\n3.Search by genre")
    print("\n4.Total")
    print("\n5.Exit")
    ch=int(input("Enter ur choice:"))
    if ch == 5:
        print("Thank u for using this app!")
        break
    elif ch == 1:
        title = input("Enter the title of the book:")
        author = input("Enter the authors name:")
        genre = input("Enter the genre of the book:")
        book = {
            "title" : title,
            "author" : author,
            "genre" : genre,
        }
        total = total+1
        books.append(book)
    elif ch == 2:
        for data in books:
            print(f"Title : {data['title']}")
            print(f"Author : {data['author']}")
            print(f"Genre : {data['genre']}")
            
    elif ch == 3:
        inputgenre = input("Enter the genre of the books u r interested in:")
        for data in books:
            if data["genre"] == inputgenre:
                print(f"Title : {data['title']}")
                print(f"Author : {data['author']}")
                print(f"Genre : {data['genre']}")
    elif ch == 4:
        print(f"Total no. of books={total}")
    else:
        print("Invalid Input!")

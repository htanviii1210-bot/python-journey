import json

try:
    with open("movies.json","r") as file:
        movies = json.load(file)
except:
    movies = []
while True:
    print("\n1. Add Movie")
    print("\n2. View All Movies")
    print("\n3. Search Movie")
    print("\n4. Total Movies")
    print("\n5. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 5:
        print("Thank u for using Movie Tracker v2!")
        break
    elif ch == 1:
        name = input("Enter the name of the movie:")
        genre = input("Enter the genre:")
        rate = int(input("Enter the rating of the movie:"))
        movie = {
            "name" : name,
            "genre" : genre,
            "rate" : rate
        }
        movies.append(movie)
        with open("movies.json","w") as file:
            json.dump(movies,file)
        print("Info has been added successfully!")
    elif ch == 2:
        for m in movies:
            print(f"Name: {m['name']} , Genre: {m['genre']} , Rating: {m['rate']}")
    elif ch == 3:
        title = input("Enter the name of the movie:")
        flag = False
        for m in movies:
            if title == m['name']:
                print(f"Name: {m['name']} , Genre: {m['genre']} , Rating: {m['rate']}")
                flag = True
        if flag == False:
                print("Not Found!")
    elif ch == 4:
        print(f"Total entries={len(movies)}")
    else:
        print("Invalid Input!")
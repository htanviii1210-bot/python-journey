#Add movie
#View All
#Search by genre
#Show Total
#Exit
print("Welcome To The Movie Tracker!")
movies = []
total = 0
while True:
    print("\n1.Add movie")
    print("\n2.View All")
    print("\n3.Search by genre")
    print("\n4.Show Total")
    print("\n5.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 5:
        print("Thank u for using The Movie Tracker!")
        break
    elif ch == 1:
        name  = input("Enter the name of the movie:")
        genre  = input("Enter the genre of the movie:")
        rate  = int(input("Enter the rating of the movie:"))
        movie = {
            "name" : name,
            "genre" : genre,
            "rate" : rate,
        }
        total = total+1
        movies.append(movie)
    elif ch == 2:
        for data in movies:
            print(f"\nMovie Name : {data['name']}")
            print(f"\nGenre : {data['genre']}")
            print(f"\nRating : {data['rate']}")
    elif ch == 3:
        inputgenre = input("Enter the genre ur interested in:")
        for data in movies:
            if data['genre'] == inputgenre:
                print(f"\nMovie Name : {data['name']}")
                print(f"\nGenre : {data['genre']}")
                print(f"\nRating : {data['rate']}")
    elif ch == 4:
        print(f"Total Movies: {total}")
    else:
        print("Invalid Input!")



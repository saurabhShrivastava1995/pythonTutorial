
movies = []

def add_new_movie():
    print("Enter the movie details")
    movie_values = []
    movie_attributes = ['name', 'director', 'year']
    for movie_attribute in movie_attributes:
        movie_values.append(input(f'Enter the attribute value "{movie_attribute}" : '))
    movies.append(dict(zip(movie_attributes, movie_values)))


def find_movie(key,value):
    count = 0
    for movie in movies:
        if movie[key] == value:
            print (movie)
    if count == 0:
        print("Sorry! No movies found for the given keyword")


while True:
    print("1. Add a new movie to the database")
    print("2. Find movies in the database")
    print("3. Exit")
    ans = input("Enter your choice : ")
    if ans == '1':
        add_new_movie()
    elif ans == '2':
        key = input("Enter the keyword : " )
        value = input("Enter the value : ")
        find_movie(key,value)
    else:
        break

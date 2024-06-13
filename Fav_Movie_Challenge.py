movies = [
    'The Shawshank Redemption',
    'The Godfather',
    'The Dark Knight',
    '12 Angry Men',
    "Schindler's List",
    'The Lord of the Rings: The Return of the King',
    'Pulp Fiction',
    'The Good, the Bad and the Ugly',
    'Fight Club',
    'Forrest Gump'
]

#Step 1 Print the movie name in sentence
for fav_mov in movies:
    print(f'My favourite Movie is {fav_mov}')

#Step 2: Firts 4, last 3, and 3 to 9 movies

print("First 4 Movies",movies[:4])
#print("last 3 Movies",movies[7:])
print("last 3 Movies",movies[-3:])

print("Movies from 3 to 9 Movies",movies[3:10])

print()

#create the list of numbers
number = []
for i in range(1, len(movies) +1):
    number.append(i)
print(number)

print()
#4 Create the list of Tuples
number_movie_tuple = []
for i in range(len(movies)):
    t = (number[i], movies[i])
    number_movie_tuple.append(t)

print()

for movie_tuple in number_movie_tuple:
    print(movie_tuple)

print()

#5 Print out the movies name from the list of Tuples

for movie_tuple in number_movie_tuple:
    print(f'I love watching {movie_tuple[1]}')

print()

#Use Enumerate on our list
for index, Value in enumerate(movies):
    print(f'index: {index}, value: {Value}')

#use enumarate we can create the list of tuples

enumerated_movies_tuple = []
for index, value in enumerate(movies):
    enumerated_movies_tuple.append(index +1, value)

for movie_tuple in enumerated_movies_tuple:
    print(movie_tuple)

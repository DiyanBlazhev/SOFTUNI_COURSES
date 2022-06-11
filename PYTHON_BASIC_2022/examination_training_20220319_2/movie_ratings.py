import sys

count_of_movies = int(input())
min_rating = sys.maxsize
min_movie = ""
max_rating = -sys.maxsize
max_movie = ""

total_rating = 0

for movie in range(count_of_movies):
    name_of_movie = input()
    rating = float(input())
    total_rating += rating
    if rating > max_rating:
        max_rating = rating
        max_movie = name_of_movie
    elif rating < min_rating:
        min_rating = rating
        min_movie = name_of_movie
average_rating = total_rating / count_of_movies
print(f"{max_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")

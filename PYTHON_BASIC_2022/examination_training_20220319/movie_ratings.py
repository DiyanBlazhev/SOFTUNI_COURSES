#•	Брой филми, които си е набелязала Деси – цяло число в интервала [1…20]
#За всеки филм се прочитат два отделни реда:
#•	Име на филма – текст
#•	Рейтинг на филма - реално число в интервала [1.00…10.00]
import sys

count_of_movies = int(input())
max_rating = -sys.maxsize
min_rating = sys.maxsize
min_rating_movie = ""
max_rating_movie = ""
sum_of_rating = 0
for movie in range(count_of_movies):
    movie_name = input()
    movie_rating = float(input())
    sum_of_rating += movie_rating

    if movie_rating > max_rating:
        max_rating_movie = movie_name
        max_rating = movie_rating
    if movie_rating < min_rating:
        min_rating_movie = movie_name
        min_rating = movie_rating

average_rating = sum_of_rating / count_of_movies
print(f"{max_rating_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")




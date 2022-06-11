name_of_movie = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_per_ticket = float(input())
percent_for_cinema = int(input())
total_profit = 0
profit_per_day = number_of_tickets * price_per_ticket
total_profit = profit_per_day * number_of_days
total_profit -= total_profit * percent_for_cinema / 100
print(f"The profit from the movie {name_of_movie} is {total_profit:.2f} lv.")

name_of_movie = input()
count_of_days = int(input())
count_of_tickets = int(input())
price_per_ticket = float(input())
percentage_for_cinema = int(input())


profit_per_day = price_per_ticket * count_of_tickets
total_profit = profit_per_day * count_of_days
final_profit = total_profit - (total_profit * (percentage_for_cinema / 100))
print(f"The profit from the movie {name_of_movie} is {final_profit:.2f} lv.")

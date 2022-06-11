budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_add_coast = int(input())


if number_of_nights > 7:
    price_per_night -= price_per_night * 0.05

cost = price_per_night * number_of_nights
additional_cost = budget * (percent_add_coast / 100)
total_sum = cost + additional_cost
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Ivanovi will be left with {diff:0.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")


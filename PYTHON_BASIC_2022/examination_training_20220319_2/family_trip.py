budget = float(input())
count_of_nights = int(input())
price_per_night = float(input())
percentage_of_additional_cost = int(input())
additional_cost = budget * (percentage_of_additional_cost / 100)
if count_of_nights > 7:
    price_per_night -= price_per_night * 0.05
cost = price_per_night * count_of_nights + additional_cost
diff = abs(budget - cost)
if cost <= budget:
    print(f"Ivanovi will be left with {diff:.02f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
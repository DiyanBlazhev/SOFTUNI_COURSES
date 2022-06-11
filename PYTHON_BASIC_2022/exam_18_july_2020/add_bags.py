price_for_bags_over_20_kg = float(input())
weight_of_bags = float(input())
days_to_traveling = int(input())
count_of_bags = int(input())
price_for_one_bag = 0

if weight_of_bags < 10:
    price_for_one_bag = price_for_bags_over_20_kg * 0.2
    if days_to_traveling > 30:
        price_for_one_bag += price_for_one_bag * 0.1
    elif 7 <= days_to_traveling <= 30:
        price_for_one_bag += price_for_one_bag * 0.15
    elif days_to_traveling < 7:
        price_for_one_bag += price_for_one_bag * 0.4

if 10 <= weight_of_bags <= 20:
    price_for_one_bag = price_for_bags_over_20_kg * 0.5
    if days_to_traveling > 30:
        price_for_one_bag += price_for_one_bag * 0.1
    elif 7 <= days_to_traveling <= 30:
        price_for_one_bag += price_for_one_bag * 0.15
    elif days_to_traveling < 7:
        price_for_one_bag += price_for_one_bag * 0.4

if weight_of_bags > 20:
    price_for_one_bag = price_for_bags_over_20_kg
    if days_to_traveling > 30:
        price_for_one_bag += price_for_one_bag * 0.1
    elif 7 <= days_to_traveling <= 30:
        price_for_one_bag += price_for_one_bag * 0.15
    elif days_to_traveling < 7:
        price_for_one_bag += price_for_one_bag * 0.4

total_price_of_bags = price_for_one_bag * count_of_bags
print(f"The total price of bags is: {total_price_of_bags:.2f} lv. ")
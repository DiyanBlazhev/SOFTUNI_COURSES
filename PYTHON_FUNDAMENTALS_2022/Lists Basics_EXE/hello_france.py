items_with_price = input().split("|")
budget = float(input())

train_ticket_cost = 150
list_of_new_prices = []
list_of_old_prices = []
for item in items_with_price:
    each_item = item.split("->")
    type_of_item = each_item[0]
    price_of_item = each_item[1]
    price_of_item = float(price_of_item)
    if type_of_item == "Clothes" and price_of_item <= 50.00 and budget >= price_of_item:
        budget -= price_of_item
        new_price = price_of_item + (price_of_item * 0.4)
        list_of_new_prices.append(new_price)
        list_of_old_prices.append(price_of_item)
    elif type_of_item == "Shoes" and price_of_item <= 35.00 and budget >= price_of_item:
        budget -= price_of_item
        new_price = price_of_item + (price_of_item * 0.4)
        list_of_new_prices.append(new_price)
        list_of_old_prices.append(price_of_item)
    elif type_of_item == "Accessories" and price_of_item <= 20.50 and budget >= price_of_item:
        budget -= price_of_item
        new_price = price_of_item + (price_of_item * 0.4)
        list_of_new_prices.append(new_price)
        list_of_old_prices.append(price_of_item)
    else:
        continue
profit = sum(list_of_new_prices) - sum(list_of_old_prices)
total_budget = budget + sum(list_of_new_prices)

string_of_new_prices = " ".join(format(x, "1.2f") for x in list_of_new_prices)

print(f"{string_of_new_prices}")
print(f"Profit: {profit:.2f}")
if total_budget >= train_ticket_cost:
    print("Hello, France!")
else:
    print("Not enough money.")

budget = float(input())

product_counter = 0
total_price = 0
while True:
    name_of_product = input()
    if name_of_product == "Stop":
        print(f"You bought {product_counter} products for {total_price:.2f} leva.")
        break
    price_of_product = float(input())
    product_counter += 1
    if product_counter % 3 == 0:
        price_of_product = price_of_product / 2
    total_price += price_of_product

    diff = abs(budget - total_price)
    if total_price > budget:
        product_counter -=1
        print(f"You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break

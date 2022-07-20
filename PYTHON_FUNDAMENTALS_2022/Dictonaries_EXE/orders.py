products = {}
command = input().split()

while command[0] != "buy":
    product, price, quantity = command
    if product not in products.keys():
        products[product] = []
        products[product].append(float(price))
        products[product].append(int(quantity))
    else:
        products[product][1] += int(quantity)
        if float(price) != products[product][0]:
            products[product][0] = float(price)


    command = input().split()
for product, total_prices in products.items():
    total_price = total_prices[0] * total_prices[1]
    print(f"{product} -> {total_price:.2f}")

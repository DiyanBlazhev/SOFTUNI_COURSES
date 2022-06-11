def orders_func(product: str, quantity: int):
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    return quantity * price


type_of_product = input()
product_quantity = int(input())
print(f"{orders_func(type_of_product, product_quantity):.2f}")

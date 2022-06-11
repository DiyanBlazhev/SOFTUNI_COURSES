count_of_order = int(input())
type_of_order = input()
delivery_way = input()
price_without_discount = 0
total_order_sum = 0

if count_of_order <= 10:
    print("Invalid order")
else:
    if type_of_order == "90X130":
        price_without_discount = count_of_order * 110
        total_order_sum = price_without_discount
        if 30 < count_of_order < 60:
            total_order_sum = price_without_discount - price_without_discount * 0.05
        elif count_of_order >= 60:
            total_order_sum = price_without_discount - price_without_discount * 0.08
        elif delivery_way == "With delivery":
            total_order_sum += 60

    if type_of_order == "100X150":
        price_without_discount = count_of_order * 140
        total_order_sum = price_without_discount
        if 40 < count_of_order < 80:
            total_order_sum = price_without_discount - price_without_discount * 0.06
        elif count_of_order >= 80:
            total_order_sum = price_without_discount - price_without_discount * 0.1
        if delivery_way == "With delivery":
            total_order_sum += 60

    if type_of_order == "130X180":
        price_without_discount = count_of_order * 190
        total_order_sum = price_without_discount
        if 20 < count_of_order < 50:
            total_order_sum = price_without_discount - price_without_discount * 0.07
        elif count_of_order >= 50:
            total_order_sum = price_without_discount - price_without_discount * 0.12
        if delivery_way == "With delivery":
            total_order_sum += 60

    if type_of_order == "200X300":
        price_without_discount = count_of_order * 250
        total_order_sum = price_without_discount
        if 25 < count_of_order < 50:
            total_order_sum = price_without_discount - price_without_discount * 0.09
        elif count_of_order >= 50:
            total_order_sum = price_without_discount - price_without_discount * 0.14
        if delivery_way == "With delivery":

            total_order_sum += 60
    if count_of_order >= 99:
        total_order_sum -= total_order_sum * 0.04
    print(f"{total_order_sum:.2f} BGN")
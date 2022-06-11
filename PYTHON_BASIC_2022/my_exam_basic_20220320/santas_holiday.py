days_staying = int(input())
type_of_room = input()
evaluation = input()
nights = days_staying - 1
price = 0
mid_price = price * nights
total_price = price * nights
if type_of_room == "room for one person":
    price = 18


if type_of_room == "apartment":
    price = 25
    if days_staying < 10:
        price -= price * 0.3
    if 10 <= days_staying <= 15:
        price -= price * 0.35
    if days_staying > 15:
        price -= price * 0.5


if type_of_room == "president apartment":
    price = 35
    if days_staying < 10:
        price -= price * 0.1
    if 10 <= days_staying <= 15:
        price -= price * 0.15
    if days_staying > 15:
        price -= price * 0.2

total_price = price * nights
if evaluation == "positive":
    total_price += total_price * 0.25
elif evaluation == "negative":
    total_price -= total_price * 0.1
print(f"{total_price:.2f}")
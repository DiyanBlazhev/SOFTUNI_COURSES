available_sum = float(input())
gender = input()
age = int(input())
sport = input()
price = 0
if gender == "m":
    if sport == "Gym":
        price = 42
        if age <= 19:
            price = 42 - 42 * 0.2
    if sport == "Boxing":
        price = 41
        if age <= 19:
            price = 41 - 41 * 0.2
    if sport == "Yoga":
        price = 45
        if age <= 19:
            price = 45 - 45 * 0.2
    if sport == "Zumba":
        price = 34
        if age <= 19:
            price = 34 - 34 * 0.2
    if sport == "Dances":
        price = 51
        if age <= 19:
            price = 51 - 51 * 0.2
    if sport == "Pilates":
        price = 39
        if age <= 19:
            price = 39 - 39 * 0.2

if gender == "f":
    if sport == "Gym":
        price = 35
        if age <= 19:
            price = 35 - 35 * 0.2
    if sport == "Boxing":
        price = 37
        if age <= 19:
            price = 37 - 37 * 0.2
    if sport == "Yoga":
        price = 42
        if age <= 19:
            price = 42 - 42 * 0.2
    if sport == "Zumba":
        price = 31
        if age <= 19:
            price = 31 - 31 * 0.2
    if sport == "Dances":
        price = 53
        if age <= 19:
            price = 53 - 53 * 0.2
    if sport == "Pilates":
        price = 37
        if age <= 19:
            price = 37 - 37 * 0.2
if available_sum >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    diff = abs(price - available_sum)
    print(f"You don't have enough money! You need ${diff:.2f} more.")

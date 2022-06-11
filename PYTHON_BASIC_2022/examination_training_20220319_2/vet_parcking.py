count_of_days = int(input())
count_of_hours = int(input())

total_price = 0
for day in range(1, count_of_days + 1):
    price = 0
    for hour in range(1, count_of_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price += 2.5
            total_price += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price += 1.25
            total_price += 1.25
        else:
            price += 1
            total_price += 1
    print(f"Day: {day} - {price:.2f} leva")
print(f"Total: {total_price:.2f} leva")
available_sea = int(input())
available_mountain = int(input())
saled_tickets_sea = 0
saled_tickets_mountain = 0
total_sum = 0
while True:
    excursion = input()
    if excursion == "Stop":
        break

    if excursion == "sea":

        saled_tickets_sea += 1
        if saled_tickets_sea <= available_sea:
            total_sum += 680
    if excursion == "mountain":
        saled_tickets_mountain += 1
        if saled_tickets_mountain <= available_mountain:
            total_sum += 499
    if saled_tickets_sea >= available_sea and saled_tickets_mountain >= available_mountain:
        break

if saled_tickets_sea >= available_sea and saled_tickets_mountain >= available_mountain:
    print(f"Good job! Everything is sold.")

print(f"Profit: {int(total_sum)} leva.")



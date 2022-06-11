vacation_money = float(input())
real_money = float(input())
total_days = 0
days_spending = 0
days_saving = 0
sum_spending = 0
sum_saving = 0
total_sum = real_money
while True:
    spend_or_save = input()
    sum = float(input())
    if spend_or_save == "spend":
        days_spending += 1
        total_days += 1

        total_sum -= sum
        if total_sum <= 0:
            total_sum = 0

    if spend_or_save == "save":
        days_saving += 1
        total_days += 1
        total_sum += sum
        days_spending = 0
    if total_sum >= vacation_money:
        print(f"You saved the money for {total_days} days.")
        break
    if days_spending == 5:
        print("You can't save the money.")
        print(total_days)
        break

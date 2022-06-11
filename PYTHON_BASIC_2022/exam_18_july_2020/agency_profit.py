name = input()
count_of_standatd_tickets = int(input())
count_of_children_ticket = int(input())
price_for_standard_ticket = float(input())
fee = float(input())
profit = 0
price_of_children_ticket = price_for_standard_ticket - price_for_standard_ticket * 0.7

total_sum = (count_of_standatd_tickets * (price_for_standard_ticket + fee))+ (count_of_children_ticket * (price_of_children_ticket + fee))

profit = total_sum * 0.2

print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")

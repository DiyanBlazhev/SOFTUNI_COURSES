poket_money = float(input())
saved_money_per_day = float(input())
all_expences = float(input())
gift_price = float(input())

save_poket_money = 5 * poket_money
saved_from_sales = 5 * saved_money_per_day
all_saved_money = save_poket_money + saved_from_sales
total_saved_money = all_saved_money - all_expences

if total_saved_money >= gift_price:
    print(f"Profit: {total_saved_money:.2f} BGN, the gift has been purchased.")
else:
    diff = gift_price - total_saved_money
    print(f"Insufficient money: {diff:.2f} BGN.")
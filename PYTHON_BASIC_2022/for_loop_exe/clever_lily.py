age_lily = int(input())
washing_machine_price = float(input())
toy_price = int(input())

even_sum = 0
toy_sum = 0
for i in range(1, age_lily + 1):
    if i % 2 == 0:
        even_sum += (10 * (i / 2)) - 1
    else:
        toy_sum += toy_price
total_sum = even_sum + toy_sum
diff = abs(washing_machine_price - total_sum)
if total_sum >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")



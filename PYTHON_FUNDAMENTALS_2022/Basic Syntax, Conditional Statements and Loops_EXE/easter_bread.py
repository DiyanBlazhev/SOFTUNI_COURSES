budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price_per_loaf = (flour_price + flour_price * 0.25) / 4

current_bread_count = 0
count_of_coloured_eggs = 0
left_money = budget
loaf_price = flour_price + eggs_price + milk_price_per_loaf
while left_money > loaf_price:
    left_money -= loaf_price
    current_bread_count += 1
    count_of_coloured_eggs += 3
    if current_bread_count % 3 == 0:
        count_of_coloured_eggs -= current_bread_count - 2
print(f"You made {current_bread_count} loaves of Easter bread! Now you have {count_of_coloured_eggs} eggs and \
{left_money:.2f}BGN left.")

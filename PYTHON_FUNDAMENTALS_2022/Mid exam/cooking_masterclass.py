import math
from math import floor, ceil


budget = float(input())
number_of_students = int(input())
price_of_flour = float(input())
price_of_single_egg = float(input())
price_of_single_apron = float(input())


flour_counter = 1
free_packages = number_of_students // 5
total_price = price_of_single_apron * (number_of_students + ceil( number_of_students * 0.2)) + (price_of_single_egg * 10 * number_of_students) + price_of_flour * (number_of_students - free_packages)

diff = abs(total_price - budget)
if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{diff:.2f}$ more needed.")
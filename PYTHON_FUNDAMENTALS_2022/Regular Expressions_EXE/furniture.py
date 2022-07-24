import re

pattern = r">>([A-za-z]+)<<(\d+\.?\d*)!(\d+)"
total_cost = 0
bought_furniture = []
command = input()
while command != "Purchase":
    match = re.search(pattern,command)
    if match:
        furniture, price, quantity = match.groups()

        total_cost += int(quantity) * float(price)
        bought_furniture.append(furniture)

    command = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
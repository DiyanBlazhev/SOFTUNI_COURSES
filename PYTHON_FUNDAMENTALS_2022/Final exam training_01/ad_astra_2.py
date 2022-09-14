import re
food_string = input()
available_food = {}
total_calories = 0


pattern = r"[\#][A-Za-z?\s]+[\#][0-9]{2}\/[0-9]{2}\/[0-9]{2}[\#](?:10000|[0-9]\d{0,3})[\#]|[\|][A-Za-z?\s]+[\|][0-9]{2}\/[0-9]{2}\/[0-9]{2}[\|](?:10000|[0-9]\d{0,3})[\|]"
result = re.findall(pattern, food_string)
new_pattern = r"\#|\|"
for item in result:
    item = re.split(new_pattern, item)
    if item[1] not in available_food:
        available_food[item[1]] = [item[2], int(item[3])]
        total_calories += int(item[3])
    else:
        available_food[item[1]][0] = item[2]
        available_food[item[1]][1] += int(item[3])
        total_calories += int(item[3])

food_days = total_calories // 2000


print(f"You have food to last you for: {food_days} days!")
for food, values in available_food.items():
    print(f"Item: {food}, Best before: {values[0]}, Nutrition: {values[1]}")
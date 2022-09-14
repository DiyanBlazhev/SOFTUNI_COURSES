import re

content_input = input()
pattern = r"([#|\|])([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.finditer(pattern,content_input)
total_cal = 0
info = []
for m in matches:
    item = m.group(2)
    date_exp = m.group(3)
    calories = int(m.group(4))
    total_cal += calories
    info.append(f'Item: {item}, Best before: {date_exp}, Nutrition: {calories}')


print(f"You have food to last you for: {int(total_cal / 2000)} days!")
[print(i) for i in info]
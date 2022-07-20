import re

phone_numbers = input()

match_phone_numbers = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
search_phone_number = re.findall(match_phone_numbers, phone_numbers)

print(", ".join(search_phone_number))
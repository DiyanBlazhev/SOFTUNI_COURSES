import re
destinations = input()
available_destinations = []
sum_of_lengths = 0
pattern = r'[\=][A-Z][A-Za-z]{2,}[\=]|[\/][A-Z][A-Za-z]{2,}[\/]'
result = re.findall(pattern, destinations)
new_pattern = r'\w+'
for item in result:
    item = re.findall(new_pattern, item)
    item = "".join(item)
    sum_of_lengths += len(item)
    available_destinations.append(item)
print(f"Destinations: {', '.join(available_destinations)}")
print(f"Travel Points: {sum_of_lengths}")
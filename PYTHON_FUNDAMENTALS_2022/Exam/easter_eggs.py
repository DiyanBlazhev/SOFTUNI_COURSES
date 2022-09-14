import re

string = input()

#pattern = r"(\@+|\#+)([a-z]{3,})(\@+|\#+)(?:[\W|\D]*)([\/]+)(\d+)([\/]+)"
#pattern = r"(\@+|\#+|[\@\#]+)([a-z]{3,})(\@+|\#+)(?:[\W|\D]*)([\/]+)(\d+)([\/]+)"
pattern = r"(\@+|\#+|[\@\#]+)([a-z]{3,})(\@+|\#+)([^0-9a-zA-Z]*)([\/]+)([0-9]+)([\/]+)"
result = re.finditer(pattern, string)

for m in result:
    colour = m.group(2)
    amount = m.group(6)
    print(f"You found {amount} {colour} eggs!")

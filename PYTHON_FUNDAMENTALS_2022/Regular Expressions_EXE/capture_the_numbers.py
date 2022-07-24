import re
digits = []
line = input()

while True:
    if line:
        pattern = r"\d+"
        result = re.findall(pattern, line)
        if result:
            digits += result
    else:
        break
    line = input()

print(" ".join(digits))

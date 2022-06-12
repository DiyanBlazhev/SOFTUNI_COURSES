string = input()
converted_string = []
numbers = list(string.split(" "))

for num in numbers:
    num = int(num) * (-1)
    converted_string.append(num)
print(converted_string)
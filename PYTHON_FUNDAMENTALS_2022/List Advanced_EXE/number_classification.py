numbers_as_string = input().split(", ")
numbers_as_digits = [int(number) for number in numbers_as_string]
print(f"Positive: {', '.join(number for number in numbers_as_string if int(number) >= 0)}")
print(f"Negative: {', '.join(number for number in numbers_as_string if int(number) < 0)}")
print(f"Even: {', '.join(number for number in numbers_as_string if int(number) % 2 == 0)}")
print(f"Odd: {', '.join(number for number in numbers_as_string if int(number) % 2 != 0)}")
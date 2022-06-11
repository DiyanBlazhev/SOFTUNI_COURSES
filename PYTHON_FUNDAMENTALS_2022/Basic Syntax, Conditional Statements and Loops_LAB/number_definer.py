number = float(input())

type_of_number = ""
amount_of_number = ""
total_number = ""
if number == 0:
    total_number = "zero"
    print(total_number)
if number > 0:
    type_of_number = "positive"
if 0 < abs(number) < 1:
    amount_of_number = "small "
if abs(number) > 1000000:
    amount_of_number = "large "
if number < 0:
    type_of_number = "negative"

total_number = amount_of_number + type_of_number
print(total_number)




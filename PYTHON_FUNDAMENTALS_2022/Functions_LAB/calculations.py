def calculation_func(number_a, number_b, operation):
    result = None
    if operation == "multiply":
        result = number_a * number_b
    elif operation == "divide":
        result = number_a / number_b
    elif operation == "add":
        result = number_a + number_b
    elif operation == "subtract":
        result = number_a - number_b
    return int(result)


type_of_operation = input()
first_number = int(input())
second_number = int(input())
print(calculation_func(first_number, second_number, type_of_operation))


def odd_even_num_finder(numbers_):
    odd_nums_sum = 0
    even_nums_sum = 0
    for num in numbers_:
        if int(num) % 2 == 0:
            even_nums_sum += int(num)
        else:
            odd_nums_sum += int(num)
    return odd_nums_sum, even_nums_sum

numbers = input()

print(f"Odd sum = {odd_even_num_finder(numbers)[0]}, Even sum = {odd_even_num_finder(numbers)[1]}")
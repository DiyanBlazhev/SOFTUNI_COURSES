some_string = input().split()
char = 0
final_sum_list = []
number = ""
divide_num = 0
multiply_num = 0
subtract_num = 0
add_num = 0
total_sum = 0


def position(alphabet):
    return ord(alphabet) - 96


for string in some_string:

    for i in range(1, len(string)-1):
        number += string[i]




    if string[0].isupper():
        divide_num = position(string[0].lower())

    elif string[0].islower():
        multiply_num = position(string[0].lower())

    if string[-1].isupper():
        subtract_num = position(string[-1].lower())

    elif string[-1].islower():
        add_num = position(string[-1].lower())
    total_sum = int(number)
    if divide_num != 0:
        total_sum /= int(divide_num)
    elif multiply_num != 0:
        total_sum *= int(multiply_num)
    if subtract_num != 0:
        total_sum -= int(subtract_num)
    elif add_num != 0:
        total_sum += int(add_num)
    final_sum_list.append(total_sum)
    divide_num = 0
    multiply_num = 0
    subtract_num = 0
    add_num = 0
    number = ""
    total_sum = 0

print(f"{sum(final_sum_list):.2f}")






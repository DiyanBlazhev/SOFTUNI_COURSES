number = input()

for first_num in range(1, int(number[2]) +1):
    for second_num in range(1, int(number[1]) + 1):
        for third_num in range(1, int(number[0]) + 1):
            print(f"{first_num} * {second_num} * {third_num} = {(first_num * second_num * third_num)};")
start_of_range = int(input())
end_of_range = int(input())
magic_number = int(input())
combination_counter = 0
flag = False
for num1 in range(start_of_range, end_of_range + 1):
    for num2 in range(start_of_range, end_of_range +1):
        combination_counter += 1
        if num1 + num2 == magic_number:
            print(f"Combination N:{combination_counter} ({num1} + {num2} = {magic_number})")
            flag = True
            break
    if flag:
        break
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
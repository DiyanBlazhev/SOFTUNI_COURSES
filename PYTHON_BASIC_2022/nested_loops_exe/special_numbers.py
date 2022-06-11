num = int(input())
special_number = 0
for first_number in range(1,10):
    for second_number in range(1,10):
        for third_number in range(1,10):
            for fourth_number in range(1,10):
                if num % first_number == 0 and num % second_number == 0 \
                        and num % third_number == 0 and num % fourth_number == 0:
                    print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")


number = int(input())

for n in range(1, number + 1):
    def get_sum():
        str_of_num = str(n)
        list_of_numbers = list(map(int, str_of_num.strip()))
        return sum(list_of_numbers)

    if get_sum() % 5 == 0 or get_sum() % 7 == 0 or get_sum() % 11 == 0:
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")




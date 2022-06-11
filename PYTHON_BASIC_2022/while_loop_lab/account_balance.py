acount_sum = 0

while True:
    increase_sum = input()

    if increase_sum == "NoMoreMoney":
        break
    if float(increase_sum) <= 0:
        print(f"Invalid operation!")
        break
    acount_sum += float(increase_sum)
    increase_sum = float(increase_sum)
    print(f"Increase: {increase_sum:.2f}")
print(f"Total: {acount_sum:.2f}")

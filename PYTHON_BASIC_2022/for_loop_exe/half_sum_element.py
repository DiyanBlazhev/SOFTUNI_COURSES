import sys
n = int(input())
max_sum = -sys.maxsize
total_sum = 0
for i in range(n):
    current_num = int(input())
    if current_num > max_sum:
        max_sum = current_num
    total_sum += current_num
if (total_sum - max_sum) == max_sum:
    print("Yes")
    print(f"Sum = {max_sum}")
else:
    diff = abs((total_sum - max_sum) - max_sum)
    print("No")
    print(f"Diff = {diff}")


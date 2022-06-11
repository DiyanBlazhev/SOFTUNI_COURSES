n = int(input())
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(n):
    current_number = int(input())
    if current_number < 200:
        num_1 += 1
        p1 = num_1 / n * 100

    if 200 <= current_number <= 399:
        num_2 += 1
        p2 = num_2 / n * 100


    if 400 <= current_number <= 599:
        num_3 += 1
        p3 = num_3 / n * 100

    if 600 <= current_number <= 799:
        num_4 += 1
        p4 = num_4 / n * 100

    if current_number >= 800:
        num_5 += 1
        p5 = num_5 / n * 100


print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
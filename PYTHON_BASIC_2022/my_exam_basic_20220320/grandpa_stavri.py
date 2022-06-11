days = int(input("days for destilation"))
sum_rakia = 0
sum_degrees = 0

for day in range(1, days + 1):
    quantity = float(input("Rakia_litters"))
    degree = float(input("degrees"))
    sum_rakia += quantity
    sum_degrees += degree * quantity
average_degree = sum_degrees / sum_rakia

print(f"Liter: {sum_rakia:.2f}")
print(f"Degrees: {average_degree:.2f}")
if average_degree < 38:
    print("Not good, you should baking!")
elif 38 <= average_degree <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
number_of_steps = int(input())


tank_capacity = 255
poored_liters = 0
for i in range(number_of_steps):
    liters = int(input())
    tank_capacity -= liters
    if tank_capacity < 0:
        tank_capacity += liters
        print("Insufficient capacity!")
        continue
    poored_liters += liters
print(poored_liters)
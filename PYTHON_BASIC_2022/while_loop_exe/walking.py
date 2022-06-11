

sum_of_steps = 0

while sum_of_steps < 10000:
    steps = input()
    if steps == "Going home":
        additional_steps = int(input())
        sum_of_steps += additional_steps
        break

    sum_of_steps += int(steps)
diff = abs(10000 - sum_of_steps)
if sum_of_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")












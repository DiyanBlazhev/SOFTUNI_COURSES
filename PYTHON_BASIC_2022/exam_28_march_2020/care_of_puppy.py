buied_food = int(input()) * 1000
consumed_food = 0
while True:
    eaded_food = input()
    if eaded_food == "Adopted":
        break
    eaded_food = int(eaded_food)
    consumed_food += eaded_food
diff = abs(buied_food - consumed_food)
if consumed_food <= buied_food:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")

fruit = input()
size = input()
count_of_order = int(input())

sum= 0

if fruit == "Watermelon":
    if size == "small":
        sum = 56 * 2 * count_of_order
    if size == "big":
        sum = 28.7 * 5 * count_of_order
    if 400<= sum <= 1000:
        sum -= sum * 0.15
    if sum > 1000:
        sum -= sum * 0.5

if fruit == "Watermelon":
    if size == "small":
        sum = 56 * 2 * count_of_order
    if size == "big":
        sum = 28.7 * 5 * count_of_order
    if 400<= sum <= 1000:
        sum -= sum * 0.15
    if sum > 1000:
        sum -= sum * 0.5

if fruit == "Mango":
    if size == "small":
        sum = 36.66 * 2 * count_of_order
    if size == "big":
        sum = 19.6 * 5 * count_of_order
    if 400<= sum <= 1000:
        sum -= sum * 0.15
    if sum > 1000:
        sum -= sum * 0.5

if fruit == "Pineapple":
    if size == "small":
        sum = 42.1 * 2 * count_of_order
    if size == "big":
        sum = 24.8 * 5 * count_of_order
    if 400<= sum <= 1000:
        sum -= sum * 0.15
    if sum > 1000:
        sum -= sum * 0.5

if fruit == "Raspberry":
    if size == "small":
        sum = 20 * 2 * count_of_order
    if size == "big":
        sum = 15.20 * 5 * count_of_order
    if 400<= sum <= 1000:
        sum -= sum * 0.15
    if sum > 1000:
        sum -= sum * 0.5




print(f"{sum:.2f} lv.")




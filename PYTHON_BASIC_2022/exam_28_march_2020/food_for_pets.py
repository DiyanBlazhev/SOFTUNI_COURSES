count_of_days = int(input())
total_food = float(input())
buiscuits = 0
dog_total_eaded_food = 0
cat_total_eaded_food = 0


for i in range(1, count_of_days + 1):
    dog_eated_food = int(input())
    cat_eated_food = int(input())
    if i % 3 == 0:
        buiscuits += (dog_eated_food + cat_eated_food) * 0.1
    dog_total_eaded_food += dog_eated_food
    cat_total_eaded_food += cat_eated_food
total_eaded_food = dog_total_eaded_food + cat_total_eaded_food
percentage_of_dog_eaded_food = dog_total_eaded_food / total_eaded_food * 100
percentage_of_cat_eaded_food = cat_total_eaded_food / total_eaded_food * 100
percentage_all_eaten_food = (dog_total_eaded_food + cat_total_eaded_food) / total_food * 100
print(f"Total eaten biscuits: {round(buiscuits)}gr.")
print(f"{percentage_all_eaten_food:.2f}% of the food has been eaten.")
print(f"{percentage_of_dog_eaded_food:.2f}% eaten from the dog.")
print(f"{percentage_of_cat_eaded_food:.2f}% eaten from the cat.")
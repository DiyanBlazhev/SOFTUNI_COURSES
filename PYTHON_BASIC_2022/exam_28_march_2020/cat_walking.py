walking_minutes_per_day = int(input())
count_of_walks_per_day = int(input())
calories = int(input())

burned_calories = walking_minutes_per_day * count_of_walks_per_day * 5
if burned_calories >= calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")

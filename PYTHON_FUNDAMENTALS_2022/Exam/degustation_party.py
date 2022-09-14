collection = {}
unliked_meals = 0

while True:
    command = input().split("-")
    if command[0] == 'Stop':
        break

    elif command[0] == 'Like':
        guest = command[1]
        meal = command[2]
        if guest not in collection:
            collection[guest] = [meal]

        #if meal in collection[guest]:
            #continue

        elif guest in collection and meal not in collection[guest]:
            collection[guest] += [meal]

    elif command[0] == 'Dislike':
        guest = command[1]
        meal = command[2]

        if guest not in collection:
            print(f"{guest} is not at the party.")

        elif meal not in collection[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")

        elif guest in collection:
            for i in collection[guest]:
                if i == meal:
                    collection[guest].remove(i)
            unliked_meals += 1
            print(f"{guest} doesn't like the {meal}.")

for name, meals in collection.items():
    if not name:
        continue
    elif not meals:
        print(f"{name}:")
    else:
        print(f"{name}: {', '.join(meals)}")
print(f"Unliked meals: {unliked_meals}")

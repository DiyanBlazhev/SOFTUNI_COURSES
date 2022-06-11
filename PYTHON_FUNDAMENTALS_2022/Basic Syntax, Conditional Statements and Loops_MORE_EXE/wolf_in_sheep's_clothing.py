animals = input()

list_of_animals = []
split_animals = animals.split(", ")
split_animals.reverse()
sheep_counter = 0
for animal in split_animals[::]:
    if animal == "wolf" and sheep_counter == 0:
        print("Please go away and stop eating my sheep")
        break
    elif animal == "sheep":
        sheep_counter += 1
    elif animal == "wolf":
        print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")

















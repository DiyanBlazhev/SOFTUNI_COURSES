word = input()

count_sand = word.lower().count("sand")
count_water = word.lower().count("water")
count_fish = word.lower().count("fish")
count_sun = word.lower().count("sun")
total = count_sun + count_fish + count_water + count_sand
print(total)

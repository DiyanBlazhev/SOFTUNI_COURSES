capacity_of_storage = float(input())
total_suitcase_volume = 0
count_of_load = 0
diff = capacity_of_storage - total_suitcase_volume
while True:
    suitcase_volume = input()
    if suitcase_volume == "End":
        print(f"Congratulations! All suitcases are loaded!")
        break
    suitcase_volume = float(suitcase_volume)
    total_suitcase_volume += suitcase_volume
    count_of_load += 1
    if count_of_load % 3 == 0:
        total_suitcase_volume += suitcase_volume * 0.1

    if total_suitcase_volume > capacity_of_storage:
        count_of_load -= 1
        print("No more space!")
        break
print(f"Statistic: {count_of_load} suitcases loaded.")

groups_number = int(input())
people_musala = 0

people_monblan = 0

people_kilimand = 0

people_k2 = 0

people_everest = 0
total_sum = 0

for i in range(1, groups_number + 1):
    count_of_peope = int(input())
    total_sum += count_of_peope
    if count_of_peope <= 5:
        people_musala += count_of_peope

    elif 6 <= count_of_peope <= 12:
        people_monblan += count_of_peope

    elif 13 <= count_of_peope <= 25:
        people_kilimand += count_of_peope

    elif 26 <= count_of_peope <= 40:
        people_k2 += count_of_peope

    elif count_of_peope >= 41:
        people_everest += count_of_peope

print(f"{(people_musala / total_sum * 100):.2f}%")
print(f"{(people_monblan / total_sum * 100):.2f}%")
print(f"{(people_kilimand / total_sum * 100):.2f}%")
print(f"{(people_k2 / total_sum * 100):.2f}%")
print(f"{(people_everest / total_sum * 100):.2f}%")

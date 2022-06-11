count_of_groups = int(input())
total_peple = 0
musala = 0
monblan = 0
kilimand = 0
k2 = 0
everest = 0
for people in range(1, count_of_groups + 1):
    count_of_people = int(input())
    if count_of_people <= 5:
        musala += count_of_people
        total_peple += count_of_people
    elif 6 <= count_of_people <= 12:
        monblan += count_of_people
        total_peple += count_of_people
    elif 13 <= count_of_people <= 25:
        kilimand += count_of_people
        total_peple += count_of_people
    elif 26<= count_of_people <= 40:
        k2 += count_of_people
        total_peple += count_of_people
    elif count_of_people >= 41:
        everest += count_of_people
        total_peple += count_of_people

print(f"{(musala / total_peple * 100):.2f}%")
print(f"{(monblan / total_peple * 100):.2f}%")
print(f"{(kilimand / total_peple * 100):.2f}%")
print(f"{(k2 / total_peple * 100):.2f}%")
print(f"{(everest / total_peple * 100):.2f}%")


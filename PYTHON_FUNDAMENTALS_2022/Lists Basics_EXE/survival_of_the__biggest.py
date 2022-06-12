list_of_number = input().split()
count_for_removing = int(input())

integers_list = list(map(int, list_of_number))

for number in range(count_for_removing):
    min_number = min(integers_list)
    integers_list.remove(min_number)
final_string = ", ".join(str(string) for string in integers_list)
print(final_string)

numbers = list(map(int, input().split(", ")))
group = 10
while len(numbers) > 0:
        group_list = list(filter(lambda x: x <= group, numbers))
        print(f"Group of {group}'s: {group_list}")

        numbers = list(filter(lambda x: x not in group_list, numbers))
        group += 10
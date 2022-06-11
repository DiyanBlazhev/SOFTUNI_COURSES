word = input()
upper_list = []
for index, char in enumerate(word):
    if char.isupper():
        upper_list.append(index)

print(upper_list)


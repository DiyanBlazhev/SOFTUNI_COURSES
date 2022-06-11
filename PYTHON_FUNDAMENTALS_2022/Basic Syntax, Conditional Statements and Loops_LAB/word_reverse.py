word = input()
reverse_word = ""
for index in word[::-1]:
    reverse_word += index
print(reverse_word)
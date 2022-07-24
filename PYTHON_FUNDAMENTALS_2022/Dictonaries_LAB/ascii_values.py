characters = input().split(", ")


char_dict = {key: ord(key) for key in characters}
print(char_dict)

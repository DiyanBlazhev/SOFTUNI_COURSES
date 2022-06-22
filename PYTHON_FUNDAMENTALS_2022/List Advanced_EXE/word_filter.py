words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
string_filtered = '\n'.join(filtered_words)

print(string_filtered)

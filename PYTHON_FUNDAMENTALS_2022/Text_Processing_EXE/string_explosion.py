text = input()
strength = 0
new_text = ""
for i in range(len(text)):
    if strength > 0 and text[i] != ">":
        strength -= 1

    elif text[i] == ">":
        strength += int(text[i + 1])
        new_text += text[i]
    else:
        new_text += text[i]


print(new_text)
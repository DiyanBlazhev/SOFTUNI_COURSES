



text = input()

new_text = ""
for i in range(0 ,len(text)):
    if int(i+1) == len(text):
        new_text += text[i]
        break
    if text[i] != text[i+1]:
        new_text += text[i]


print(new_text)


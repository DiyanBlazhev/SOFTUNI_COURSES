text = input()
emoticon = []
for i in  range(len(text)):
    if text[i] == ":":
        emoticon += [":" + text[i + 1]]

print(f"\n".join(emoticon))



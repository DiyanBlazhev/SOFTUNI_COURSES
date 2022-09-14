text = input()
encrypted_text = ""

for ch in text:
    ascii_num = ord(ch) + 3
    encrypted_text += chr(ascii_num)
print(encrypted_text)


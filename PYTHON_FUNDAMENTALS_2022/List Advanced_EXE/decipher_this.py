message = input().split()
final_message = []
for message in message:
    num = ""
    current_message = ""
    for digit in message:
        if digit.isdigit():
            num += digit
        else:
            break
    message = message.replace(num, "")
    num = int(num)
    current_message += chr(num)
    if len(message) >= 2:
        message = message[-1] + message[1:-1] + message[0]
    current_message += message
    final_message.append(current_message)
print(" ".join(final_message))




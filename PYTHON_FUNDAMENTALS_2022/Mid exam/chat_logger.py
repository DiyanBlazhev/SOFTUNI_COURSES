new_message = []
while True:

    command = input().split()
    if command[0] == "end":
        break

    if command[0] == "Chat":
        new_message.append(command[1])
    elif command[0] == "Delete":
        for word in new_message:
            if word == command[1]:
                new_message.remove(word)
            else:
                continue
    elif command[0] == "Edit":
        for i in enumerate(new_message):
            if i[1] == command[1]:
                new_message[i[0]] = command[2]
            else:
                continue

    elif command[0] == "Pin":
        for p in enumerate(new_message):
            if p[1] == command[1]:
                new_str = new_message.pop(p[0])
                new_message.append(new_str)


            else:
                continue
    elif command[0] == "Spam":
        command.remove(command[0])
        for char in command:
            new_message.append(char)
str_new_message = " \n".join(new_message)
print(str_new_message)

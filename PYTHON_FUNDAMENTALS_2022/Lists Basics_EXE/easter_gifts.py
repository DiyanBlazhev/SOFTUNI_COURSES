names_of_the_gifts = input().split()

gifts = []
command = ""
while command != "No Money":
    command = input()
    command_separator = command.split()
    type_of_command = command_separator[0]
    gift_in_command = command_separator[1]


    if type_of_command == "OutOfStock":
        for i in range(len(names_of_the_gifts)):
            if names_of_the_gifts[i] == gift_in_command:
                names_of_the_gifts[i] = None

    elif type_of_command == "Required":

        replace_gift = command_separator[1]
        index_of_gift = int(command_separator[2])
        for i in range(len(names_of_the_gifts)):

            if i == index_of_gift:
                names_of_the_gifts[i] = replace_gift
            else:
                continue
    elif type_of_command == "JustInCase":

        replace_gift = command_separator[1]
        names_of_the_gifts[-1] = replace_gift
names_of_the_gifts = list(filter(None, names_of_the_gifts))
final_gifts = " ".join(str(i) for i in names_of_the_gifts)
print(final_gifts)

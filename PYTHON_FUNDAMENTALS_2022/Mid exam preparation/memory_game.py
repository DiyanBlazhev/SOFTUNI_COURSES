elements = input().split()
command = ""
move_counter = 1
while True:
    command = input()
    if command == "end":
        break

    list_command = list(map(int, command.split()))
    if list_command[0] == list_command[1] or list_command[0] > len(elements) or list_command[0] < 0 or list_command[1] < 0:
        inserting_index = int(len(elements) / 2)
        elements.insert(inserting_index, f"-{move_counter}a")
        elements.insert(inserting_index, f"-{move_counter}a")
        print("Invalid input! Adding additional elements to the board")
        continue
    elif elements[list_command[0]] == elements[list_command[1]]:
        elem_for_del = [list_command[0], list_command[1]]
        for index in sorted(elem_for_del, reverse=True):
            removed = elements.pop(index)

        print(f"Congrats! You have found matching elements - {removed}!")
    else:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {move_counter} turns!")
        break
    move_counter += 1
if len(elements) > 0:
    str_elements = " ".join(elements)
    print(f"Sorry you lose :(\n{str_elements}")
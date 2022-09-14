breaks = input()
while True:
    command = input().split(":")
    if command[0] == "Travel":
        break

    elif command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index <= len(breaks):
            breaks = breaks[:index] + string + breaks[index:]
            print(breaks)
        else:
            print(breaks)


    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= len(breaks)-1 and 0 <= end_index <= len(breaks)-1:
            breaks = breaks[:start_index] + breaks[end_index + 1:]
            print(breaks)
        else:
            print(breaks)


    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in breaks:
            breaks = breaks.replace(old_string, new_string)
            print(breaks)
        else:
            print(breaks)




print(f"Ready for world tour! Planned stops: {breaks}")
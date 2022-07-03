sequence = list(map(int, input().split()))

while True:

    command = input().split()
    if command[0] == "Finish":
        break
    elif command[0] == "Add":
        sequence.append(int(command[1]))
        continue
    elif command[0] == "Remove":
        for n in sequence:
            if n == int(command[1]):
                new3_index = sequence.index(int(command[1]))
                sequence.pop(new3_index)
                continue
    elif command[0] == "Replace":
        for i in sequence:
            if i == int(command[1]):
                new_index = sequence.index(i)
                sequence[new_index] = int(command[2])
                break

    elif command[0] == "Collapse":
        sequence = [x for x in sequence if x >= int(command[1])]

new_sequence = list(map(str, sequence))
print(" ".join(new_sequence))

data = input()

while True:
    command = input().split(" ")
    if command[0] == "Finish":
        break

    elif command[0] == "Replace":
        data = data.replace(command[1], command[2])
        print(data)

    elif command[0] == "Cut":
        if 0 < int(command[1]) <= len(data) and 0 < int(command[2]) <= len(data):
            data = data[:int(command[1])] + data[int(command[2])+1:]
            print(data)
        else:
            print("Invalid indices!")

    elif command[0] == "Make":
        if command[1] == "Upper":
            data = data.upper()
        elif command[1] == "Lower":
            data = data.lower()
        print(data)

    elif command[0] == "Check":
        if command[1] in data:
            print(f"Message contains {command[1]}")
        else:
            print(f"Message doesn't contain {command[1]}")

    elif command[0] == "Sum":
        if 0 > int(command[1]) or int(command[1]) > len(data) or 0 > int(command[2]) or int(command[2]) > len(data):
            print("Invalid indices!")
        else:
            sum_char = 0
            substring = data[int(command[1]):int(command[2])+1]
            for ch in substring:
                sum_char += ord(ch)
            print(sum_char)



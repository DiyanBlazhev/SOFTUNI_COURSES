password = input()
raw_password = ""
while True:
    command = input().split()
    if command[0] == "Done":
        print(f"Your password is: {raw_password}")
        break
    elif command[0] == "TakeOdd":

        for i in range(len(password)):

            if i % 2 != 0:
                raw_password += password[i]

        print(raw_password)

    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        raw_password = raw_password[:index] + raw_password[index + length:]
        print(raw_password)

    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print("Nothing to replace!")


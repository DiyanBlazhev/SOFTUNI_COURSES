users = {}
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    type_of_command = command[0]
    name = command[1]
    if type_of_command == "register":
        plate_number = command[2]
        if name not in users.keys():
            users[name] = 0
            users[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {users[name]}")

    elif type_of_command == "unregister":
        if name not in users.keys():
            print(f"ERROR: user {name} not found")
        else:
            del users[name]
            print(f"{name} unregistered successfully")

for user, plate in users.items():
    print(f"{user} => {plate}")


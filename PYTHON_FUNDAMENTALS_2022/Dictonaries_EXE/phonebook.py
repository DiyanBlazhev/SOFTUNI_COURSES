phonebook = {}

while True:
    entry = input()
    if not "-" in entry:
        break
    name, phone = entry.split("-")
    phonebook[name] = phone
for checking in range(int(entry)):
    searching_contact = input()
    if searching_contact in phonebook.keys():
        print(f"{searching_contact} -> {phonebook[searching_contact]}")
    else:
        print(f"Contact {searching_contact} does not exist.")
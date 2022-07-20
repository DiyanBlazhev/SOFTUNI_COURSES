users = {}
lang_counter = {}
command = input()
while command != "exam finished":
    command = command.split("-")
    if len(command) == 3:
        name = command[0]
        lang = command[1]
        points = command[2]
        if name not in users.keys() and lang not in lang_counter:
            users[name] = [lang, int(points)]
            lang_counter[lang] = 0
            lang_counter[lang] += 1
        else:
            lang_counter[lang] += 1
            if name not in users.keys():
                users[name] = [lang, int(points)]
            elif lang in users[name][0] and users[name][1] < int(points):
                users[name][1] = points
    else:
        users.pop(name)
    command = input()
print("Results:")
for user,points in users.items():
    print(f"{user} | {points[1]}")
print("Submissions:")
for language, subm in lang_counter.items():
    print(f"{language} - {subm}")

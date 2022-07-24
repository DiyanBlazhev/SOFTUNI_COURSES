students = {}
corresponding_course = ""
command = input().split(":")
while len(command) != 1:
    name = command[0]
    student_id = command[1]
    course = command[2]
    students[name] = [student_id, course]
    command = input().split(":")
if len(command) == 1:
    split_command = " ".join(command)
    split_command = split_command.replace("_", " ")
    corresponding_course = split_command

for name, id_course in students.items():
    if id_course[1] == corresponding_course:
        print(f"{name} - {id_course[0]}")

courses = {}
command = input().split(" : ")

while command[0] != "end":
    course, name = command
    if course not in courses.keys():
        courses[course] = []
        courses[course] = [name]
    else:
        courses[course].append(name)

    command = input().split(" : ")

for current_course in courses.keys():
    print(f"{current_course}: {len(courses[current_course])}")
    for student_name in courses[current_course]:
        [print(f"-- {student_name}")]

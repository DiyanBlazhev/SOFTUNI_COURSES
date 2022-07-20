students = {}
command = int(input())

for _ in range(command):

    name = input()
    grade = float(input())
    if name in students.keys():
        if grade not in students[name]:
            students[name].append(grade)
    else:
        students[name] = [grade]
new_students = students.copy()
for student, grades in students.items():
    average_grade = sum(grades)/len(grades)
    new_students[student] = average_grade
    if average_grade < 4.50:
        del new_students[student]

for name, average_grade in new_students.items():
    print(f"{name} -> {average_grade:.2f}")




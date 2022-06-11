name = input()
class_counter = 0
sum_grades = 0
excludes = 0
excluses_condition = False

while class_counter < 12:
    grade = float(input())
    if grade < 4:
        excludes += 1
        if excludes > 1:
            excluses_condition = True
            class_counter +=1
            break
    else:
        sum_grades += grade
        class_counter += 1
if excluses_condition:
    print(f"{name} has been excluded at {class_counter} grade")
else:
    average_grade = sum_grades / class_counter
    print(f"{name} graduated. Average grade: {average_grade:.2f}")

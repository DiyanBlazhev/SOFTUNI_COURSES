n = int(input())
flag = False
sum_of_grades = 0
average_grade = 0
sum_of_all_grades = 0
counter = 0
while True:
    presentation_name = input()
    if presentation_name == "Finish":
        flag = True
        break
    for _ in range(1, n + 1):
        grade = float(input())
        sum_of_grades += grade
        sum_of_all_grades += grade
        counter += 1
    average_grade = sum_of_grades / n
    sum_of_grades = 0
    print(f"{presentation_name} - {average_grade:.2f}.")


final_assessment = sum_of_all_grades / counter
print(f"Student's final assessment is {final_assessment:.2f}.")


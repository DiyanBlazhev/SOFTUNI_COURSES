max_bad_grades = int(input())

grade_counter = 0
bad_grades = 0
sum_of_grades = 0
last_problem = ""
failed_or_not = True
task_name = ""

while True:
    task_name = input()

    if task_name == "Enough":
        average_grade = sum_of_grades / grade_counter
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {grade_counter}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())
    grade_counter += 1
    sum_of_grades += grade
    if grade <= 4:
        bad_grades += 1
    if bad_grades == max_bad_grades:
        print(f"You need a break, {bad_grades} poor grades.")
        break
    last_problem = task_name



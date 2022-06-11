count_of_open_tabs = int(input())
salary = float(input())

last_salary = salary
for web_name in range(1, count_of_open_tabs + 1):
    web_name = input()
    if web_name == "Facebook":
        last_salary -= 150
    elif web_name == "Instagram":
        last_salary -= 100
    elif web_name == "Reddit":
        last_salary -= 50
    if last_salary <= 0:
        print("You have lost your salary.")
        break
if last_salary > 0:
    print(f"{int(last_salary)}")

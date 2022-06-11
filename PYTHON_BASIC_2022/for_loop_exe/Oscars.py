actor_name = input()
academy_points = float(input())
count_of_evaluators = int(input())
total_points = academy_points
for i in range(1, count_of_evaluators + 1):
    name_of_evaluator = input()
    points = float(input())
    total_points += points * len(name_of_evaluator) / 2
    if total_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    diff = abs(1250.5 - total_points)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")


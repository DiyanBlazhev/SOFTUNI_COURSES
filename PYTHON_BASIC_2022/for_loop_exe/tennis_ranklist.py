from math import floor

count_of_games = int(input())
start_points = int(input())
sum_of_points = 0
win_games = 0


for i in range(1, count_of_games + 1):
    ranking = input()
    if ranking == "W":
        sum_of_points += 2000
        win_games += 1
    elif ranking == "F":
        sum_of_points += 1200
    elif ranking == "SF":
        sum_of_points += 720

average_points = sum_of_points / count_of_games
percentage_win_games = win_games / count_of_games * 100
print(f"Final points: {sum_of_points + start_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percentage_win_games:.2f}%")
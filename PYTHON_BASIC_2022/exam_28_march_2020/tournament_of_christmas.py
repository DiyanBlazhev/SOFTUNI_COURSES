count_of_tournaments_days = int(input())
sport = ""
win_games = 0
lose_games = 0
win_money_per_day = 0
total_win_games = 0
total_lose_games = 0
total_sum = 0
for i in range(count_of_tournaments_days):

    while True:
        sport = input()
        if sport == "Finish":
            break
        result = input()
        if result == "win":
            win_games += 1
            win_money_per_day += 20
            total_win_games += 1
        else:
            lose_games += 1
            total_lose_games += 1
    if win_games > lose_games:
        win_money_per_day += win_money_per_day * 0.1
    win_games = 0
    lose_games = 0
    total_sum += win_money_per_day
    win_money_per_day = 0
if total_win_games > total_lose_games:
    total_sum += total_sum * 0.2
    print(f"You won the tournament! Total raised money: {total_sum:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_sum:.2f}")


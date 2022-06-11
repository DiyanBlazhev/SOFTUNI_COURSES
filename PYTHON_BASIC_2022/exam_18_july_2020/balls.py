count_of_balls = int(input())

total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_colour_balls = 0
devided_times_black = 0

for ball in range(count_of_balls):
    colour_of_ball = input()
    if colour_of_ball == "red":
        red_balls += 1
        total_points += 5
    elif colour_of_ball == "orange":
        orange_balls += 1
        total_points += 10
    elif colour_of_ball == "yellow":
        yellow_balls += 1
        total_points += 15
    elif colour_of_ball == "white":
        white_balls += 1
        total_points += 20
    elif colour_of_ball == "black":
        devided_times_black += 1
        total_points /= 2
    else:
        other_colour_balls += 1
print(f"Total points: {int(total_points)}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_colour_balls}")
print(f"Divides from black balls: {devided_times_black}")

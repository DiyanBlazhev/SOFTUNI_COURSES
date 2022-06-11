width = int(input())
length = int(input())
height = int(input())

free_place = width * length * height
left_space = 0

while True:
    box_volume = input()
    if box_volume == "Done":
        break
    left_space += int(box_volume)
    if left_space > free_place:
        break

diff = abs(left_space - free_place)
if free_place >= left_space:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(diff)} Cubic meters more.")
def chairs_checker(room):
    left_chairs = 0
    command = True
    for num_room in range(1, number_of_rooms +1):
        rooms = input().split(" ")
        chairs = len(list(rooms[0]))
        visitors = int(rooms[1])
        needed_chairs_in_room = abs(visitors - chairs)

        if visitors > chairs:
            needed_chairs_in_room = abs(visitors - chairs)
            print(f"{needed_chairs_in_room} more chairs needed in room {num_room}")
            command = False
        else:
            left_chairs += (chairs - visitors)
    if command:
        print(f"Game On, {left_chairs} free chairs left")


number_of_rooms = int(input())
chairs_checker(number_of_rooms)
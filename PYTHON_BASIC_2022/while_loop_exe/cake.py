width = int(input())
length = int(input())
eaded_pieces = ""
cake_pieces = (width * length)
left_pieces = cake_pieces
while eaded_pieces != "STOP":
    if left_pieces <= 0:
        diff = abs(left_pieces)
        print(f"No more cake left! You need {diff} pieces more.")
        break
    eaded_pieces = (input())
    if eaded_pieces == "STOP":
        print(f"{left_pieces} pieces are left.")
        break
    left_pieces -= int(eaded_pieces)



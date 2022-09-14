def creation_list_of_pieces(list_of_pieces, number):
    for _ in range(number):
        data = input().split("|")
        piece = data[0]
        composer = data[1]
        key = data[2]
        list_of_pieces[piece] = [composer, key]
    return list_of_pieces


def modify_list_of_pieces(list_of_pieces):
    while True:
        command = input().split("|")
        if command[0] == 'Stop':
            break
        elif command[0] == 'Add':
            if command[1] not in list_of_pieces:
                list_of_pieces[command[1]] = [command[2], command[3]]
                print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
            else:
                print(f"{command[1]} is already in the collection!")

        elif command[0] == 'Remove':
            if command[1] in list_of_pieces:
                del list_of_pieces[command[1]]
                print(f"Successfully removed {command[1]}!")
            else:
                print(f"Invalid operation! {command[1]} does not exist in the collection.")

        elif command[0] == 'ChangeKey':
            if command[1] in list_of_pieces:
                list_of_pieces[command[1]][1] = command[2]
                print(f"Changed the key of {command[1]} to {command[2]}!")
            else:
                print(f"Invalid operation! {command[1]} does not exist in the collection.")


def additional_printing(list_of_pieces):
    for piece in list_of_pieces:
        composer = list_of_pieces[piece][0]
        key = list_of_pieces[piece][1]
        print(f"{piece} -> Composer: {composer}, Key: {key}")


def main_pieces(number):
    list_of_pieces = {}

    creation_list_of_pieces(list_of_pieces, number)
    modify_list_of_pieces(list_of_pieces)
    additional_printing(list_of_pieces)


n = int(input())
main_pieces(n)


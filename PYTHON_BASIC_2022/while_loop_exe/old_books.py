favorite_book = input()
book_counter = 0
while True:
    name_of_book = input()

    if name_of_book == favorite_book:
        print(f"You checked {book_counter} books and found it.")
        break
    elif name_of_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break
    book_counter += 1



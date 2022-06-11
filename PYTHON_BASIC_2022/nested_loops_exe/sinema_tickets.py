flag = False
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
seats_counter = 0
total_tickets = 0
while True:
    movie = input()


    if movie == "Finish":
        print(f"Total tickets: {total_tickets}")
        print(f"{(student_tickets / total_tickets *100):.2f}% student tickets.")
        print(f"{(standard_tickets / total_tickets * 100):.2f}% standard tickets.")
        print(f"{(kid_tickets / total_tickets * 100):.2f}% kids tickets.")
        flag = True
        break
    free_seats = int(input())
    for _ in range(1, free_seats +1):
        ticket = input()
        if ticket == "End":
            flag = True
            break
        elif ticket == "student":
            student_tickets += 1
        elif ticket == "standard":
            standard_tickets += 1
        elif ticket == "kid":
            kid_tickets += 1
        seats_counter += 1
        total_tickets += 1

    print(f"{movie} - {(seats_counter / free_seats * 100):.2f}% full.")
    seats_counter = 0

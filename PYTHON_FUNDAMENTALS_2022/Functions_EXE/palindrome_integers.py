def palindrome_integers(integers):
    result = True
    for integer in integers:
        if integer == integer[::-1]:
            result = True
        else:
            result = False
        print(result)


number = input().split(", ")


palindrome_integers(number)



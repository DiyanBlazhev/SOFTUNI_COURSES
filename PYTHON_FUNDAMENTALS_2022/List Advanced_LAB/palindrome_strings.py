def palindrome_finder(words, palindrome):
    result = []
    for word in words:
        if word == word[::-1]:
            result.append(word)
    palindrome_counter = result.count(palindrome)

    print(result)
    print(f"Found palindrome {palindrome_counter} times")


text = input().split(" ")
secret = input()
palindrome_finder(text, secret)




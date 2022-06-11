import array as arr

number = int(input())
largest_number = ""
num = [int(x) for x in str(number)]
num.sort(reverse=True)

for i in num:
    largest_number += str(i)
print(largest_number)






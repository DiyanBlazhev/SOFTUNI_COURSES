import sys

max_number = -sys.maxsize


while True:
    numer = input()
    if numer == "Stop":
        break
    numer = int(numer)
    if numer >= max_number:
        max_number = numer

print(max_number)
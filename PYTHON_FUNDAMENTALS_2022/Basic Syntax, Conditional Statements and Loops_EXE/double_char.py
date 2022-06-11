string = ""

while True:
    string = input()
    double_char_string = ""
    if string == "SoftUni":
        continue
    elif string == "End":
        break
    for char in string[::]:
        double_char_string += char * 2
    print(double_char_string)
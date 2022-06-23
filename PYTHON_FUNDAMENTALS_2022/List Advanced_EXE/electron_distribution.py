number_of_electrons = int(input())
shells = []
counter = 0
while number_of_electrons > 0:
    counter +=1
    max_electron_in_shell = 2 * (counter * counter)
    if number_of_electrons < max_electron_in_shell:
        shells.append(number_of_electrons)
        break
    number_of_electrons -= max_electron_in_shell
    shells.append(max_electron_in_shell)
    if number_of_electrons <= 0:
        break

print(shells)
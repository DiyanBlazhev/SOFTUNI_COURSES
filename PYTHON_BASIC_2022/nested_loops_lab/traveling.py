
flag = False
vacantion_sum = 0

while True:
    destination = input()
    if destination == "End":
      flag = True
      break
    needed_money = float(input())


    while needed_money > vacantion_sum:
        saved_money = float(input())
        vacantion_sum += float(saved_money)

        if vacantion_sum >= needed_money:
            print(f"Going to {destination}!")
            vacantion_sum = 0
            flag = True
            break







procesor_price = float(input())
video_card = float(input())
ram = float(input())
count_of_ram = int(input())
discount = float(input())
procesor_in_lev = procesor_price * 1.57
video_card_in_lev = video_card * 1.57
ram_in_lev = ram * 1.57

total_ram = count_of_ram * ram_in_lev
procesor_dis = procesor_in_lev - procesor_in_lev * discount
videocadr_dis = video_card_in_lev - video_card_in_lev * discount

sum = procesor_dis + videocadr_dis + total_ram



print(f"Money needed - {sum:.2f} leva.")
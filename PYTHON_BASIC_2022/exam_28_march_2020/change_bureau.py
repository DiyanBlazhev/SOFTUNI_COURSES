bitcoins = int(input())
uans = float(input())
fee = float(input())

leva = (bitcoins * 1168) + (uans * 0.15 * 1.76)
euro =leva / 1.95
final_euro = euro - (euro * fee /100)

print(f"{final_euro:.2f}")

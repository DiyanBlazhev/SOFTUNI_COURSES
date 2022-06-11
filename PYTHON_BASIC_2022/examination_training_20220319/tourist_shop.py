#•	На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]
#•	След това поредица от два реда (до получаване на команда "Stop" или при заявка за купуване на продукт, чиято стойност е по-висока от наличния бюджет) :
#o	Име на продукта – текст
#o	Цена на продукта – реално число в интервала [1.00… 5000.00]
budget = float(input())
cost = 0
couter_of_products = 0
budget_condition = False
needed_money = 0
while True:
    name_of_product = input()
    if name_of_product == "Stop":
        break
    product_price = float(input())
    couter_of_products += 1

    if couter_of_products % 3 == 0:
        product_price /= 2
    if product_price > budget:
        budget_condition = True
        needed_money = product_price - budget
        couter_of_products -= 1
        break
    cost += product_price
    budget -= product_price
if not budget_condition:
    print(f"You bought {couter_of_products} products for {cost:.2f} leva.")
else:
    print(f"You don't have enough money!")
    print(f"You need {needed_money:.2f} leva!")

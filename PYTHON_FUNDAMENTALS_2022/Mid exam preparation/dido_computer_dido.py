total_price_without_taxes = 0
total_amount_of_taxes = 0
total_price = 0
while True:

    command = input()

    if command == "special":

        break
    if command == "regular":
        break
    float_command = float(command)
    if float_command < 0:
        print("Invalid price!")
        continue

    total_price_without_taxes += float_command


total_amount_of_taxes += total_price_without_taxes * 0.2
total_price = total_price_without_taxes + total_amount_of_taxes
if command == "special":
    total_price -= total_price * 0.1
if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: \
{total_price_without_taxes:.2f}$\nTaxes: {total_amount_of_taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")

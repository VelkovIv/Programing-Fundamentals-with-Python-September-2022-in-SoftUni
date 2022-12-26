total_price_without_vat = 0

while True :
    command = input()
    if command == 'special' or command == 'regular' :
        break
    current_price = float(command)
    if current_price < 0 :
        print('Invalid price!')
        continue
    total_price_without_vat += current_price
if total_price_without_vat == 0:
    print('Invalid order!')
else:
    total_price_with_vat = total_price_without_vat * 1.2
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price_without_vat:.2f}$')
    taxes = total_price_with_vat - total_price_without_vat
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    if command == 'special':
        total_price_with_vat *=0.9
    print(f'Total price: {total_price_with_vat:.2f}$')



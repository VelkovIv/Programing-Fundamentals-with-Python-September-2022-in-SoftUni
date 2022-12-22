products_in_stock = {}

while True :
    command = input()

    if command == 'statistics' :
        break

    product, quantity = command.split(': ')

    if product not in products_in_stock :
        products_in_stock[product] = 0

    products_in_stock[product] += int(quantity)

print("Products in stock:")
for product, quantity in products_in_stock.items() :
    print(f"- {product}: {quantity}")
print(f'Total Products: {len(products_in_stock)}')
print(f'Total Quantity: {sum(products_in_stock.values())}')

items_with_prices = input().split('|')
budget = float(input())
# updated_items_with_prices = []
profit_list = []
profit = 0
total_profit = 0
for item in items_with_prices :
    updated_items_with_prices = item.split('->')
    item_type = updated_items_with_prices[0]
    item_price = float(updated_items_with_prices[1])
    current_price = 0
    if (item_type == 'Clothes' and item_price <= 50.00) or \
            (item_type == 'Shoes' and item_price <= 35.00) or \
            (item_type == 'Accessories' and item_price <= 20.50) :
        if budget >= item_price :
            budget -= item_price
            current_price = item_price * 1.4
            profit += current_price - item_price
            print(f'{current_price:.2f}', end=" ")
            total_profit += current_price
            profit_list.append(str(current_price))
print() # print(', '.join(profit_list))
print(f'Profit: {profit:.2f}')
if total_profit + budget >= 150 :
    print('Hello, France!')
else :
    print('Not enough money.')



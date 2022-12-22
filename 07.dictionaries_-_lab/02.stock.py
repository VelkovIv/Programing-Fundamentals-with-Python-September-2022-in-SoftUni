items = input().split()
searched_products = input().split()
stock_items = {}
for index in range(0, len(items), 2) :
    key = items[index]
    value = int(items[index + 1])
    stock_items[key] = value
for product in searched_products :
    if product in stock_items :
        quantity = stock_items[product]
        print(f"We have {quantity} of {product} left")
    else :
        print(f"Sorry, we don't have {product}")

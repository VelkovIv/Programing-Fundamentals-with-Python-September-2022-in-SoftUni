items = input().split()
stock_items = {}
for index in range(0, len(items), 2) :
    key = items[index]
    value = int(items[index + 1])
    stock_items[key] = value
print(stock_items)

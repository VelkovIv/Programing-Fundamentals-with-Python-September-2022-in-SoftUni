__doc__ = """
Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
• If the product doesn't exist yet, add it with its starting quantity.
• If you receive a product, which already exists, increases its quantity by the input quantity and
if its price is different, replace the price as well.
You will receive products' names, prices, and quantities on new lines. 
Until you receive the command "buy", keep adding items.
Finally, print all items with their names and the total price of each product. 
Input
• Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
• The product data is always delimited by a single space.
Output
• Print information about each product in the following format: 
"{product_name} -> {total_price}"
• Format the total price to the 2nd digit after the decimal separator.

---Input---
Beer 2.20 100
IceTea 1.50 50
NukaCola 3.30 80
Water 1.00 500
buy

---Output---
Beer -> 220.00
IceTea -> 75.00
NukaCola -> 264.00
Water -> 500.00

---Input---
Beer 2.40 350
Water 1.25 200
IceTea 5.20 100
Beer 1.20 200
IceTea 0.50 120
buy

---Output---
Beer -> 660.00
Water -> 250.00
IceTea -> 110.00

---Input---
CesarSalad 10.20 25
SuperEnergy 0.80 400
Beer 1.35 350
IceCream 1.50 25
buy

---Output---
CesarSalad -> 255.00
SuperEnergy -> 320.00
Beer -> 472.50
IceCream -> 37.50


"""
all_products = {}
while True :
    current_product = input().split()

    if current_product[0] == 'buy' :
        break

    product_name, currrent_price, current_quantity = current_product
    currrent_price, current_quantity = float(currrent_price), int(current_quantity)

    if product_name not in all_products.keys() :
        all_products[product_name] = [0, 0]
    all_products[product_name].pop(0)
    all_products[product_name].insert(0, currrent_price)
    current_quantity += all_products[product_name].pop(1)
    all_products[product_name].insert(1,current_quantity)

for product_name, details in all_products.items() :
    total_price = details[0] * details[1]
    print(f"{product_name} -> {total_price:.2f}")

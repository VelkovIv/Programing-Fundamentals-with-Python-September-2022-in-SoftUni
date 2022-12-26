___doc___ = """
Let`s take a break and visit the game bar at SoftUni. It is about time for the people behind the bar to go home
and you are the person who has to draw the line and calculate the money from the products that
 were sold throughout the day. Until you receive a line with text "end of shift" you will be given lines of input. 
 But before processing that line you should do some validations first.
Each valid order should have a customer, product, count and a price:
•	Valid customer's name should be surrounded by '%' and must start with a capital letter, followed by lower-case letters
•	Valid product contains any word character (not only letters) and must be surrounded by '<' and '>' 
•	Valid count is an integer, surrounded by '|'
•	Valid price is any real number followed by '$'
The parts of a valid order should appear in the order given: customer, product, count and a price.
Between each part there can be other symbols, except ('|', '$', '%' and '.')
For each valid line print on the console: "{customerName}: {product} - {totalPrice}"
When you receive "end of shift" print the total amount of money for the day rounded to
2 decimal places in the following format: "Total income: {income}".
Input / Constraints
•	Strings that you have to process until you receive text "end of shift".
Output
•	Print all of the valid lines in the format "{customerName}: {product} - {totalPrice}"
•	After receiving "end of shift" print the total amount of money for the day rounded
to 2 decimal places in the following format: "Total income: {income}"
•	Allowed working time / memory: 100ms / 16MB.


---------------------------------------------------
Examples
---------------------------------------------------
--->Input
%George%<Croissant>|2|10.3$
%Peter%<Gum>|1|1.3$
%Maria%<Cola>|1|2.4$
end of shift

Output--->
George: Croissant - 20.60
Peter: Gum - 1.30
Maria: Cola - 2.40
Total income: 24.30

---------------------------------------------------
--->Input
%InvalidName%<Croissant>|2|10.3$
%Peter%<Gum>1.3$
%Maria%<Cola>|1|2.4
%Valid%<Valid>valid|10|valid20$
end of shift

Output--->
Valid: Valid - 200.00
Total income: 200.00

---------------------------------------------------
"""

import re

total_income = 0
pattern_customer_name = r'%([A-Z][a-z]+)%'
pattern_product = r'<(\w+)>'
pattern_quantity = r'\|(\d+)\|'
pattern_price = r'(\d+\.?\d+?)\$'

while True:

    current_command = input()

    if current_command == 'end of shift':
        break

    customer_name = re.findall(pattern_customer_name, current_command)
    product = re.findall(pattern_product, current_command)
    quantity = re.findall(pattern_quantity, current_command)
    price = re.findall(pattern_price, current_command)
    total_price = 0

    if customer_name and product and quantity and price:
        total_price = float(price[0]) * int(quantity[0])

        print(f'{customer_name[0]}: {product[0]} - {total_price:.2f}')

        total_income += total_price

print(f'Total income: {total_income:.2f}')

___doc___ = """
Write a program that calculates the total cost of bought furniture. You will be given information about each purchase on separate lines until you receive the command "Purchase". Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer number. You should store the names of the furniture and the total price. 
In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
"Bought furniture:
{1st name}
{2nd name}
…
{N name}
Total money spend: {total_cost}"


---------------------------------------------------
Examples
---------------------------------------------------
--->Input
>>Sofa<<312.23!3
>>TV<<300!5
>Invalid<<!5
Purchase

Output--->
Bought furniture:
Sofa
TV
Total money spend: 2436.69

---------------------------------------------------
"""

import re

pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
bought_furniture = []
total_cost = 0

while True:
    current_input = input()

    if current_input == 'Purchase':
        break

    current_furniture = re.search(pattern, current_input)

    if current_furniture:
        furniture, price, quantity = current_furniture.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)

print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {total_cost:.2f}')

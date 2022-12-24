__doc__ = """
You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
•	"Shadowmourne" - requires 250 Shards
•	"Valanyr" - requires 250 Fragments
•	"Dragonwrath" - requires 250 Motes
"Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk. 
You will be given lines of input in the format: 
"{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
Keep track of the key materials - the first one that reaches 250, wins the race. 
At that point, you have to print that the corresponding legendary item is obtained. 
In the end, print the remaining shards, fragments, motes in the format:
"shards: {number_of_shards}
fragments: {number_of_fragments}
motes: {number_of_motes}"
Finally, print the collected junk items in the order of appearance.
Input
•	Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
Output
•	On the first line, print the obtained item in the format: "{Legendary item} obtained!"
•	On the next three lines, print the remaining key materials 
•	On the several final lines, print the junk items
•	All materials should be printed in the format: "{material}: {quantity}"
•	The output should be lowercase, except for the first letter of the legendary


---Input---
3 Motes 5 stones 5 Shards
6 leathers 255 fragments 7 Shards

---Output---
Valanyr obtained!
shards: 5
fragments: 5
motes: 3
stones: 5
leathers: 6

---Input---
123 silver 6 shards 8 shards 5 motes
9 fangs 75 motes 103 MOTES 8 Shards
86 Motes 7 stones 19 silver

---Output---
Dragonwrath obtained!
shards: 22
fragments: 0
motes: 19
silver: 123
fangs: 9

"""

inventory = {"shards" : 0, "fragments" : 0, "motes" : 0}
ithem_obtained = False
while not ithem_obtained :
    current_items = input().split()

    for index in range(0, len(current_items), 2) :
        value = int(current_items[index])
        key = current_items[index + 1].lower()

        if key not in inventory.keys():
            inventory[key] = 0

        inventory[key] += value

        if inventory['shards'] >= 250:
            inventory['shards'] -= 250
            print("Shadowmourne obtained!")
            ithem_obtained = True

        elif inventory['fragments'] >= 250:
            inventory['fragments'] -= 250
            print("Valanyr obtained!")
            ithem_obtained = True

        elif inventory['motes'] >= 250:
            inventory['motes'] -= 250
            print("Dragonwrath obtained!")
            ithem_obtained = True

        if ithem_obtained:
            break

for material, quantity in inventory.items():
    print(f"{material}: {quantity}")
___doc___ = """
You will be given a sequence of strings, each on a new line until you receive the "stop" command. 
Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and
every even - quantity. Your task is to collect the resources and print them each on a new line.
Print the resources and their quantities in the following format:
"{resource} -> {quantity}"
The quantities will be in the range [1 … 2 000 000 000].

--Input--
Gold
155
Silver
10
Copper
17
stop
----------
--Output--
Gold -> 155
Silver -> 10
Copper -> 17

--Input--
gold
155
silver
10
copper
17
gold
15
stop

--Output--
gold -> 170
silver -> 10
copper -> 17

"""

items = {}
while True :
    command = input()
    if command == "stop" :
        break

    for i in range(1) :
        key = command
        value = int(input())

        if value == "stop" :
            command = value
            break

        if key not in items.keys() :
            items[key] = 0
        items[key] += value

for resource, quantity in items.items():
    print(f"{resource} -> {quantity}")
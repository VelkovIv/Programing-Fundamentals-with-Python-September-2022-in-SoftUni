target_cities = {}

while True:  # start to collect target cities
    collecting_command = input().split('||')

    if collecting_command[0] == 'Sail':
        break

    city, population, gold = collecting_command[0], int(collecting_command[1]), int(collecting_command[2])

    if city not in target_cities:
        # create target city if not in a dictionary and store in a list population (index 0) and gold index 1
        # if the city is in the dictionary for population and gold the new values are add to the existing
        target_cities[city] = [0, 0]

    target_cities[city][0] += population
    target_cities[city][1] += gold

while True:

    action_command = input().split('=>')

    if action_command[0] == 'End':
        break

    town = action_command[1]

    if action_command[0] == 'Plunder':
        people, gold = int(action_command[2]), int(action_command[3])

        target_cities[town][0] -= people
        target_cities[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')

        if target_cities[town][0] <= 0 or target_cities[town][1] <= 0:
            print(f'{town} has been wiped off the map!')
            del target_cities[town]

    elif action_command[0] == 'Prosper':
        gold = int(action_command[2])

        if gold >= 0:
            target_cities[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {target_cities[town][1]} gold.')
        else:
            print('Gold added cannot be a negative number!')

if len(target_cities) == 0:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    print(f'Ahoy, Captain! There are {len(target_cities)} wealthy settlements to go to:')

    for city, stats in target_cities.items():
        print(f'{city} -> Population: {stats[0]} citizens, Gold: {stats[1]} kg')

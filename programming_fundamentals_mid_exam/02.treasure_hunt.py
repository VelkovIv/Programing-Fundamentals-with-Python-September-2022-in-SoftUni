def loot_func(treasure_chest, current_command) :
    current_command.pop(0)

    for element in current_command :
        if element not in treasure_chest :
            treasure_chest.insert(0, element)

    return treasure_chest


def drop_func(treasure_chest, index) :
    if 0 <= index < len(treasure_chest) :
        treasure_chest.append(treasure_chest.pop(index))

    return treasure_chest


initial_treasure_chest = input().split('|')
is_chest_empty = False

while True :
    command = input()
    if command == 'Yohoho!' :
        break
    current_command = command.split(' ')

    if current_command[0] == 'Loot' :
        initial_treasure_chest = loot_func(initial_treasure_chest, current_command)

    elif current_command[0] == 'Drop' :
        initial_treasure_chest = drop_func(initial_treasure_chest, int(current_command[1]))

    elif current_command[0] == 'Steal' :
        count = int(current_command[1])
        stealed = []

        if count >= len(initial_treasure_chest) :
            stealed = initial_treasure_chest.copy()
            # treasure_chest = []
            print(', '.join(stealed))
            is_chest_empty = True
            break
        elif count < len(initial_treasure_chest) :
            for i in range(int(count)) :
                stealed.append(initial_treasure_chest.pop())
            stealed = stealed[: :-1]
        print(', '.join(stealed))

if is_chest_empty :
    print("Failed treasure hunt.")
else :
    total_gain = 0
    for i in range(len(initial_treasure_chest)) :
        total_gain += len(initial_treasure_chest[i])
    average_gain = total_gain / len(initial_treasure_chest)
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')

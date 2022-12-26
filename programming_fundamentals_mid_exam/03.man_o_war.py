
pirate_ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
max_health_section_capacity = int(input())
is_batle_end = False
is_pirate_ship_sunken = False
while True :

    command = input()
    if command == 'Retire' :
        is_batle_end = True
        break

    current_command = command.split(' ')

    if current_command[0] == 'Fire' :
        section = int(current_command[1])
        damage = int(current_command[2])

        if 0 <= section < len(warship_status) :
            warship_status[section] -= damage
            if warship_status[section] <= 0 :
                print('You won! The enemy ship has sunken.')
                break

    elif current_command[0] == 'Defend' :
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        damage = int(current_command[3])

        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status) :
            for section in range(start_index, end_index + 1) :
                pirate_ship_status[section] -= damage

                if pirate_ship_status[section] <= 0 :
                    print('You lost! The pirate ship has sunken.')
                    is_pirate_ship_sunken = True
                    break

        if is_pirate_ship_sunken:
            break

    elif current_command[0] == 'Repair' :
        section = int(current_command[1])
        health = int(current_command[2])

        if 0 <= section < len(pirate_ship_status) :
            pirate_ship_status[section] += health
            if pirate_ship_status[section] > max_health_section_capacity :
                pirate_ship_status[section] = max_health_section_capacity


    elif current_command[0] == 'Status' :
        section_count = 0
        for section in range(len(pirate_ship_status)):
            if pirate_ship_status[section] < max_health_section_capacity * 0.2 :
                section_count += 1

        if section_count >0:
            print(f'{section_count} sections need repair.')

if is_batle_end:
    print(f'Pirate ship status: {sum(pirate_ship_status)}')
    print(f'Warship status: {sum(warship_status)}')

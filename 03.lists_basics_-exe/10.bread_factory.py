events = input().split('|')
total_coints = 100
total_energy = 100
is_open = True
for event in events :
    event_type = event.split('-')
    event_name = event_type[0]
    event_value = int(event_type[1])
    if event_name == 'rest' :
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100 :
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {total_energy}.')
    elif event_name == 'order' :
        if total_energy >= 30 :
            total_energy -= 30
            total_coints += event_value
            print(f'You earned {event_value} coins.')
        else :
            total_energy += 50
            print('You had to rest!')
    else :
        if total_coints >= event_value :
            total_coints -= event_value
            print(f'You bought {event_name}.')
        else :
            print(f'Closed! Cannot afford {event_name}.')
            is_open = False
            break
if is_open :
    print("Day completed!")
    print(f"Coins: {total_coints}")
    print(f"Energy: {total_energy}")

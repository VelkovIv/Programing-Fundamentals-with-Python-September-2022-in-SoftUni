def potion_func(initial_health, power) :
    current_health = initial_health + power

    if current_health > 100 :
        current_health = 100
        power = 100 - initial_health

    print(f'You healed for {power} hp.')
    print(f'Current health: {current_health} hp.')

    return current_health


def facing_monster_func(current_room, power, initial_health) :
    initial_health -= power

    if initial_health > 0 :
        print((f'You slayed {current_room}.'))

    return initial_health


initial_health = 100
initial_bitcoin = 0

rooms = input().split('|')
you_are_dead = False
room_counter = 0
for room in rooms :

    current_room, power = room.split(' ')
    power = int(power)
    room_counter += 1

    if current_room == 'potion' :
        initial_health = potion_func(initial_health, power)
    elif current_room == 'chest' :
        initial_bitcoin += power
        print(f'You found {power} bitcoins.')
    else :
        initial_health = facing_monster_func(current_room, power, initial_health)

    if initial_health <= 0 :
        you_are_dead = True
        break

if you_are_dead :
    print(f'You died! Killed by {current_room}.')
    print(f'Best room: {room_counter}')
else :
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoin}")
    print(f"Health: {initial_health}")

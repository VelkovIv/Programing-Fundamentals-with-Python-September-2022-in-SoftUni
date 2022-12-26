initial_energy = int(input())
won_counter = 0
end_of_the_battle = False
while True :
    command = input()
    if command == 'End of battle' :
        end_of_the_battle = True
        break
    distance_to_enemy = int(command)
    if initial_energy >= distance_to_enemy :
        initial_energy -= distance_to_enemy
        won_counter += 1
        if won_counter % 3 == 0 :
            initial_energy += won_counter
    else:
        print(f"Not enough energy! Game ends with {won_counter} won battles and {initial_energy} energy")
        break

if end_of_the_battle:
    print(f'Won battles: {won_counter}. Energy left: {initial_energy}')

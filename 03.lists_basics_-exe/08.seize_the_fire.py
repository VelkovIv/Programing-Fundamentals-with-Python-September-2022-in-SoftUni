fire_level_and_power = input().split('#')
water = int(input())
fire_level_and_power_new = []
effort = 0
total_fire = 0
print('Cells:')
for index in range(len(fire_level_and_power)) :
    current_element = fire_level_and_power[index]
    fire_level_and_power_new.append(current_element.split(' = '))
for cell in range(len(fire_level_and_power_new)) :
    if fire_level_and_power_new[cell][0] == 'High' and 81 <= int(fire_level_and_power_new[cell][1]) <= 125 :
        if water >= int(fire_level_and_power_new[cell][1]):
            water -= int(fire_level_and_power_new[cell][1])
            print(f' - {fire_level_and_power_new[cell][1]}')
            total_fire += int(fire_level_and_power_new[cell][1])
    elif fire_level_and_power_new[cell][0] == 'Medium' and 51 <= int(fire_level_and_power_new[cell][1]) <= 80:
        if water >= int(fire_level_and_power_new[cell][1]):
            water -= int(fire_level_and_power_new[cell][1])
            print(f' - {fire_level_and_power_new[cell][1]}')
            total_fire += int(fire_level_and_power_new[cell][1])
    elif fire_level_and_power_new[cell][0] == 'Low' and 1 <= int(fire_level_and_power_new[cell][1]) <= 50:
        if water >= int(fire_level_and_power_new[cell][1]):
            water -= int(fire_level_and_power_new[cell][1])
            print(f' - {fire_level_and_power_new[cell][1]}')
            total_fire += int(fire_level_and_power_new[cell][1])
effort = total_fire/4
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')


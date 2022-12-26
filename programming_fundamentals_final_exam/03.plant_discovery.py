def rate_func(plants_dict, plant_, rating_):
    if plant_ in plants_dict.keys():
        current_rating = plants_dict[plant_][1]
        if current_rating != 0:
            rating_ = (rating_ + current_rating) / 2

        plants_dict[plant_][1] = rating_
    else:
        print('error')

    return plants_dict


def update_func(plants_dict, plant_, new_rarity_):
    if plant_ in plants_dict.keys():
        plants_dict[plant_][0] = new_rarity_
    else:
        print('error')

    return plants_dict


def reset_func(plants_dict, plant_):
    if plant_ in plants_dict.keys():
        plants_dict[plant_][1] = 0
    else:
        print('error')

    return plants_dict


number_of_lines = int(input())

plants = {}

for line in range(number_of_lines):
    plant, rarity = input().split('<->')
    rarity = int(rarity)

    if plant not in plants.keys():
        plants[plant] = [0, 0]

    plants[plant] = [rarity, 0]

while True:
    current_command = input().split(': ')

    if current_command[0] == 'Exhibition':
        break

    current_info = current_command[1].split(' - ')
    plant = current_info[0]

    if current_command[0] == 'Rate':
        rating = int(current_info[1])

        plants = rate_func(plants, plant, rating)

    elif current_command[0] == 'Update':
        new_rarity = int(current_info[1])

        plants = update_func(plants, plant, new_rarity)


    elif current_command[0] == 'Reset':
        plants = reset_func(plants, plant)

print('Plants for the exhibition:')
for plant, stat in plants.items():
    print(f'- {plant}; Rarity: {stat[0]}; Rating: {stat[1]:.2f}')

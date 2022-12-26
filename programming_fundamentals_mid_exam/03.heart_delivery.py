def jump_func(place, current_position) :
    if place[current_position] == 0 :
        print(f"Place {current_position} already had Valentine's day.")
        return place, current_position

    place[current_position] -= 2

    if place[current_position] == 0 :
        print(f"Place {current_position} has Valentine's day.")
        return place, current_position


def cupid_trip_func(neighborhood, current_position) :
    while True :
        command = input()
        if command == 'Love!' :
            break

        current_command = command.split(' ')
        jump_lenght = int(current_command[1])
        current_position += jump_lenght

        if current_position > len(neighborhood) -1  :
            current_position = 0

        jump_func(neighborhood, current_position)

    print(f"Cupid's last position was {current_position}.")

    if sum(neighborhood) == 0 :
        print("Mission was successful.")
    else :
        house_count = [house for house in neighborhood if house > 0]
        print(f"Cupid has failed {len(house_count)} places.")


neighborhood = list(map(int, input().split('@')))
current_position = 0
cupid_trip_func(neighborhood, current_position)

def add_stop_func(travel_stops, index, substring):
    if 0 <= index <= len(travel_stops):
        travel_stops = travel_stops[:index] + substring + travel_stops[index:]

    print(travel_stops)

    return travel_stops


def remove_stop_func(travel_stops, start_index, end_index):
    if 0 <= start_index <= end_index < len(travel_stops):
        travel_stops = travel_stops[:start_index] + travel_stops[end_index + 1:]

    print(travel_stops)

    return travel_stops


def switch_func(travel_stops, old_string, new_string):
    if old_string in travel_stops:
        travel_stops = travel_stops.replace(old_string, new_string)

    print(travel_stops)

    return travel_stops


all_stops = input()

while True:
    command = input().split(':')

    if command[0] == 'Travel':
        break

    if command[0] == 'Add Stop':
        index, substring = int(command[1]), command[2]

        all_stops = add_stop_func(all_stops, index, substring)

    elif command[0] == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])

        all_stops = remove_stop_func(all_stops, start_index, end_index)

    elif command[0] == 'Switch':
        first_string, second_string = command[1], command[2]

        all_stops = switch_func(all_stops, first_string, second_string)

print(f'Ready for world tour! Planned stops: {all_stops}')

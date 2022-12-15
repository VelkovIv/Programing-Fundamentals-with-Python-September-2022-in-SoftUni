number = int(input())
wagons = [0] * number

while True :
    command = input()
    if command == 'End' :
        break
    split_command = command.split(' ')
    currect_command = split_command[0]

    if currect_command == 'add' :
        people_to_add = int(split_command[1])
        wagons[-1] += people_to_add

    elif currect_command == 'insert' :
        wagon_number = int(split_command[1])
        people_to_add = int(split_command[2])
        wagons[wagon_number] += people_to_add

    elif currect_command == 'leave' :
        wagon_number = int(split_command[1])
        people_to_leave = int(split_command[2])
        wagons[wagon_number] -= people_to_leave
print(wagons)

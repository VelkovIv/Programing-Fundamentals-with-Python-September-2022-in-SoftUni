def shoot_func(targets, index, power) :
    if 0 <= index < len(targets) :
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)

    return targets


def add_func(targets, index, power) :
    if 0 <= index < len(targets) :
        targets.insert(index, power)
    else :
        print('Invalid placement!')

    return targets


def strike_func(targets, index, radius) :
    validator = index - radius >= 0 and index + radius < len(targets)
    if validator :
        targets1 = []
        start_index = index - radius
        final_index = index + radius

        for i in range(len(targets)) :
            if i < start_index or i > final_index :
                targets1.append(targets[i])

        return targets1
    else :
        print('Strike missed!')

        return targets


sequence_of_targets = list(map(int, input().split(' ')))

while True :
    command = input()
    if command == 'End' :
        break

    action, index, power = command.split(' ')
    index = int(index)
    power = int(power)

    if action == 'Shoot' :
        sequence_of_targets = shoot_func(sequence_of_targets, index, power)
    elif action == 'Add' :
        sequence_of_targets = add_func(sequence_of_targets, index, power)
    elif action == 'Strike' :
        sequence_of_targets = strike_func(sequence_of_targets, index, power)
print(*sequence_of_targets, sep='|')
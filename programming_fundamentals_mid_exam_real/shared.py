def prefer_func(coffees, index1, index2) :
    if 0 <= index1 < len(coffees) and 0 <= index2 < len(coffees) :
        coffees[index1], coffees[index2] = coffees[index2], coffees[index1]

    return coffees


def reverse_func(coffees) :
    coffees = coffees[: :-1]
    return coffees


coffee = input()
count = int(input())
coffees = coffee.split(' ')

for comm in range(count) :

    current_command = input().split(' ')

    if current_command[0] == 'Include' :
        coffees.append(current_command[1])

    elif current_command[0] == 'Remove' :
        possition = current_command[1]
        coffees_to_remove = int(current_command[2])

        if 0 <= coffees_to_remove < len(coffees) :

            for index in range(coffees_to_remove) :
                if possition == 'first' :
                    coffees.pop(0)
                elif possition == 'last' :
                    coffees.pop()

    elif current_command[0] == 'Prefer' :
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        coffees = prefer_func(coffees, index1, index2)
    elif current_command[0] == 'Reverse' :
        coffees = reverse_func(coffees)

print('Coffees:')
print(" ".join(coffees))

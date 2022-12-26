def include_func(coffees_in_stock,coffee):
    return coffees_in_stock.append(coffee)


def prefer_func(coffees_in_stock, index1, index2) :
    if 0 <= index1 < len(coffees_in_stock) and 0 <= index2 < len(coffees_in_stock) :
        coffees_in_stock[index1], coffees_in_stock[index2] = coffees_in_stock[index2], coffees_in_stock[index1]

    return coffees_in_stock

def reverse_func(coffees_in_stock):
    coffees_in_stock = coffees_in_stock[::-1]
    return coffees_in_stock


coffees = input()
count_of_commands = int(input())
coffees_in_stock = coffees.split(' ')
print(coffees_in_stock)
print(len(coffees_in_stock))
for comm in range(count_of_commands) :

    current_command = input().split(' ')

    if current_command[0] == 'Include' :
        coffees_in_stock = include_func(coffees_in_stock,current_command[1])

    elif current_command[0] == 'Remove' :
        possition_in_the_list = current_command[1]
        coffees_number_to_remove = int(current_command[2])

        if 0 <= coffees_number_to_remove < len(coffees_in_stock):
            if possition_in_the_list == 'first' :
                for index in range(1, len(coffees_in_stock) + 1) :
                    if index <= coffees_number_to_remove :
                        coffees_in_stock.pop(0)

            elif possition_in_the_list == 'last' :
                for index in range(len(coffees_in_stock), -1, -1) :
                    if index <= coffees_number_to_remove :
                        coffees_in_stock.pop()


    elif current_command[0] == 'Prefer' :
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        coffees_in_stock = prefer_func(coffees_in_stock, index1, index2)
    elif current_command[0] == 'Reverse' :
        coffees_in_stock = reverse_func(coffees_in_stock)

print('Coffees:')
print(" ".join(coffees_in_stock))
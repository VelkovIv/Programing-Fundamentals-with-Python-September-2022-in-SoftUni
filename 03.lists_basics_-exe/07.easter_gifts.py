names_of_the_gifts = input().split()
command = input()
while command != "No Money" :
    command_list = []
    command_list = command.split()
    command_excecution = command_list[0]
    command_value = command_list[1]
    if len(command_list) == 3 :
        command_index = int(command_list[2])
    for index, value in enumerate(names_of_the_gifts) :
        if command_excecution == 'OutOfStock' :
            if names_of_the_gifts[index] == command_value :
                names_of_the_gifts[index] = 'None'
        elif command_excecution == 'Required' :
            if index == command_index :
                names_of_the_gifts.pop(command_index)
                names_of_the_gifts.insert(command_index, command_value)
        elif command_excecution == 'JustInCase':
            names_of_the_gifts.pop()
            names_of_the_gifts.append(command_value)
    command = input()
while 'None'in names_of_the_gifts:
    names_of_the_gifts.remove('None')
print(' '.join(names_of_the_gifts))
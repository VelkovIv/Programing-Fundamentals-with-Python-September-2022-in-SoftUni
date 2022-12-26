def urgent_func(lst, item) :
    if item not in lst :
        lst.insert(0, item)
    return lst


def unnecessary_func(lst, item) :
    if item in lst :
        lst.remove(item)
    return lst


def correct_func(lst, old_item, new_iten) :
    if old_item in lst :
        index = lst.index(old_item)
        lst.remove(old_item)
        lst.insert(index, new_iten)
    return lst


def rearrange_func(lst, item) :
    if item in lst :
        lst.remove(item)
        lst.append(item)
    return lst


def shopping_list_func(shopping_list) :
    while True :
        command = input()

        if command == 'Go Shopping!' :
            break

        current_command = command.split(' ')
        current_item = current_command[1]

        if current_command[0] == 'Urgent' :
            shopping_list = urgent_func(shopping_list, current_item)
        elif current_command[0] == 'Unnecessary' :
            shopping_list = unnecessary_func(shopping_list, current_item)
        elif current_command[0] == 'Correct' :
            new_item = current_command[2]
            shopping_list = correct_func(shopping_list, current_item, new_item)
        elif current_command[0] == 'Rearrange' :
            shopping_list = rearrange_func(shopping_list, current_item)

    print(', '.join(shopping_list))


initial_list = input().split('!')
shopping_list_func(initial_list)

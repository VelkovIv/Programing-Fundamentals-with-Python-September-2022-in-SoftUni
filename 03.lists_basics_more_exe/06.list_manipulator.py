def max_func(number_new, even_odd) :
    max_even_number = -1
    max_odd_number = -1

    for index in range(len(number_new)) :
        if number_new [index] % 2 == 0 :
            if number_new[index] >= max_even_number :
                max_even_number = number_new[index]
                max_even_index = index
        else :
            if number_new[index] >= max_odd_number :
                max_odd_number = number_new[index]
                max_odd_index = index

    if even_odd == 'even' :
        if max_even_number == -1 :
            print('No matches')
        else :
            print(max_even_index)
    else :
        if max_odd_number == -1 :
            print('No matches')
        else :
            print(max_odd_index)

    return number_new


def min_func(number_new, even_odd) :
    min_even_number = -1
    min_odd_number = -1

    for index in range(len(number_new)) :
        if index % 2 == 0 :
            if number_new[index] < min_even_number :
                min_even_number = number_new[index]
                min_even_index = index
        else :
            if number_new[index] < min_odd_number :
                min_odd_number = number_new[index]
                min_odd_index = index

    if even_odd == 'even' :
        if min_even_number == -1 :
            print('No matches')
        else :
            print(min_even_index)
    else :
        if min_odd_number == -1 :
            print('No matches')
        else :
            print(min_odd_index)
    return number_new


def first_func(number_new, count, even_odd) :
    even = []
    odd = []
    if 0 <= count < len(number_new) :
        for index in range(count) :
            if even_odd == 'even' and number_new[index] % 2 == 0 :
                even.append(number_new[index])
            elif even_odd == 'odd' and number_new[index] % 2 != 0 :
                odd.append(number_new[index])

    if even_odd == 'even' :
        print(even)
    else :
        print(odd)

    return number_new


def last_func(number_new, count, even_odd) :
    even = []
    odd = []
    if 0 <= count < len(number_new) :
        for index in range(-len(number_new), -1, -1) :
            if even_odd == 'even' and number_new[index] % 2 == 0 :
                even.append(number_new[index])
            elif even_odd == 'odd' and number_new[index] % 2 != 0 :
                odd.append(number_new[index])

    if even_odd == 'even' :
        print(even)
    else :
        print(odd)

    return number_new


numbers = list(map(int, input().split(' ')))

while True :
    command = input()
    if command == 'end' :
        break

    input_command = command.split(' ')

    if input_command[0] == 'exchange' :
        slice_plice = int(input_command[1])
        if 0 <= slice_plice < len(numbers) :
            numbers = numbers[slice_plice + 1 :len(numbers)]
            numbers.extend(numbers[:slice_plice + 1])
            print(numbers)
        else :
            print('Invalid index')
    elif input_command[0] == 'max' :
        even_odd = input_command[1]
        numbers = max_func(numbers, even_odd)

    elif input_command[0] == 'min' :
        even_odd = input_command[1]
        numbers = min_func(numbers, even_odd)

    elif input_command[0] == 'first' :
        count = int(input_command[1])
        even_odd = input_command[2]
        numbers = first_func(numbers, count, even_odd)

    elif input_command[0] == 'last' :
        count = int(input_command[1])
        even_odd = input_command[2]
        numbers = last_func(numbers, count, even_odd)

print(numbers)

def swap_func(input_array, index1, index2) :
    input_array[index1], input_array[index2] = input_array[index2], input_array[index1]

    return input_array


def multiply_func(input_array, index1, index2) :
    input_array[index1] = input_array[index1] * input_array[index2]

    return input_array


def decrease_func(input_array) :
    for index in range(len(input_array)) :
        input_array[index] -= 1

    return input_array


input_array = list(map(int, input().split(' ')))

while True :
    command = input()
    if command == "end" :
        break

    current_command = command.split(' ')

    if len(current_command) > 1 :
        index1 = int(current_command[1])
        index2 = int(current_command[2])

    if current_command[0] == 'swap' :
        new_array = swap_func(input_array, index1, index2)
    elif current_command[0] == 'multiply' :
        new_array = multiply_func(input_array, index1, index2)
    elif current_command[0] == 'decrease' :
        new_array = decrease_func(input_array)

print(*new_array, sep=", ")

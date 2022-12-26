def contain_function(key, string):
    if string in key:
        print(f"{key} contains {string}")
    else:
        print(f'Substring not found!')


def flip_function(case_type, start_index, end_index, key):
    if case_type == 'Upper':
        key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
        print(key)
    elif case_type == 'Lower':
        key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
        print(key)

    return key


def slice_symbols_function(key, first_index, last_index):
    if first_index == 0:
        key = key[last_index:]
    else:
        key = key[:first_index] + key[last_index:]

    print(key)

    return key


activation_key = input()
# activation_key = ''
command = input()

while command != 'Generate':
    current_command = command.split('>>>')

    if current_command[0] == 'Contains':
        substring = current_command[1]
        contain_function(activation_key, substring)

    elif current_command[0] == 'Flip':
        case_type, start_index, end_index = current_command[1], int(current_command[2]), int(current_command[3])
        activation_key = flip_function(case_type, start_index, end_index, activation_key)

    elif current_command[0] == 'Slice':
        f_index, l_index = int(current_command[1]), int(current_command[2])
        activation_key = slice_symbols_function(activation_key, f_index, l_index)

    command = input()

print(f'Your activation key is: {activation_key}')




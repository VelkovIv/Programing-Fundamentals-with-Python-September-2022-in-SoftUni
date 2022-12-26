def take_odd_funk(password_):
    new_pass = ''
    for index in range(len(password_)):
        if index % 2 != 0:
            new_pass += password_[index]

    print(new_pass)

    return new_pass


def cut_func(password_, index_, length_):
    password_ = password_[:index_] + password_[index + length_:]

    print(password_)

    return password_


def substutute_func(password_, substring_, substitute_):
    if substring_ in password_:
        password_ = password_.replace(substring_, substitute_)
        print(password_)
    else:
        print('Nothing to replace!')

    return password_


password = input()

while True:
    current_command = input().split()

    if current_command[0] == 'Done':
        break

    if current_command[0] == 'TakeOdd':
        password = take_odd_funk(password)

    elif current_command[0] == 'Cut':
        index, length = int(current_command[1]), int(current_command[2])

        password = cut_func(password, index, length)

    elif current_command[0] == 'Substitute':
        substring, substitute = current_command[1], current_command[2]

        password = substutute_func(password, substring, substitute)

print(f'Your password is: {password}')

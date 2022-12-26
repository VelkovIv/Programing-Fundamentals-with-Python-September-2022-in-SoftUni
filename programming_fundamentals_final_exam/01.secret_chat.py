concealed_massage = input()

while True:
    command = input().split(':|:')

    if command[0] == 'Reveal':
        break

    if command[0] == 'InsertSpace':
        index = int(command[1])
        concealed_massage = concealed_massage[:index] + ' ' + concealed_massage[index:]

        print(concealed_massage)

    elif command[0] == 'Reverse':
        substring = command[1]

        if substring in concealed_massage:
            concealed_massage = concealed_massage.replace(substring, '', 1) + substring[::-1]
            print(concealed_massage)
        else:
            print('error')

    elif command[0] == 'ChangeAll':
        substring, replacement = command[1], command[2]

        concealed_massage = concealed_massage.replace(substring, replacement)

        print(concealed_massage)

print(f'You have a new text message: {concealed_massage}')

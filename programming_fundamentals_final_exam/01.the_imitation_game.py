encrypted_massage = input()

command = input()

while command != 'Decode':
    current_command = command.split('|')

    if current_command[0] == 'Move':
        number_of_letters = int(current_command[1])  # adjust to the string indexes staring from 0
        encrypted_massage = encrypted_massage[number_of_letters:] + encrypted_massage[:number_of_letters]

    elif current_command[0] == 'Insert':
        index, value = int(current_command[1]), current_command[2]
        encrypted_massage = encrypted_massage[:index] + value + encrypted_massage[index:]

    elif current_command[0] == 'ChangeAll':
        substring, replacement = current_command[1], current_command[2]
        encrypted_massage = encrypted_massage.replace(substring, replacement)

    command = input()
print(f'The decrypted message is: {encrypted_massage}')

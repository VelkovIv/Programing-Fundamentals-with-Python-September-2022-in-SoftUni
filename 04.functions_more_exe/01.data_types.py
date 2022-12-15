def action(command, value) :
    if command == 'int':
        return int(value) * 2
    elif command == 'real':
        return f'{float(value) * 1.50:.2f}'
    elif command == "string":
        return '$' + value + '$'

command = input()
number = input()
print(action(command,number))



command = input()
house_name = ''
while command != 'Welcome!':
    if command == 'Voldemort':
        print('You must not speak of that name!')
        break
    if len(command) < 5:
        house_name = 'Gryffindor.'
    elif len(command) == 5:
        house_name = 'Slytherin.'
    elif len(command) == 6:
        house_name = 'Ravenclaw.'
    else:
        house_name = 'Hufflepuff.'
    print(f'{command} goes to {house_name}')
    command = input()
else:
    print("Welcome to Hogwarts.")
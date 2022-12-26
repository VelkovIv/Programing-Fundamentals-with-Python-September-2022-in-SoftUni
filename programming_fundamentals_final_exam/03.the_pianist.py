def change_key_function(all_pieces, name, n_key):
    if name in all_pieces.keys():
        all_pieces[name][1] = n_key
        print(f'Changed the key of {name} to {n_key}!')
    else:
        print(f'Invalid operation! {name} does not exist in the collection.')


def remove_function(name, all_pieces):
    if name in all_pieces.keys():
        print(f'Successfully removed {name}!')
        del all_pieces[name]
    else:
        print(f'Invalid operation! {name} does not exist in the collection.')

    return all_pieces


def add_function(name, author, m_key, all_pieces):
    if name in all_pieces.keys():
        print(f'{name} is already in the collection!')
    else:
        all_pieces[name] = [author, m_key]
        print(f'{name} by {author} in {m_key} added to the collection!')

    return all_pieces


number_of_pieces = int(input())

pieces = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split('|')

    # creating dictionary with piece as key and list as value on index 0 is composer and on index 1 is key
    pieces[piece] = [composer, key]

while True:
    current_command = input().split('|')

    if current_command[0] == 'Stop':
        break

    piece = current_command[1]

    if current_command[0] == 'Add':
        composer, key = current_command[2], current_command[3]
        add_function(piece, composer, key, pieces)

    elif current_command[0] == "Remove":
        remove_function(piece, pieces)

    elif current_command[0] == 'ChangeKey':
        new_key = current_command[2]
        change_key_function(pieces, piece, new_key)

for piece, data in pieces.items():
    composer, key = data[0], data[1]
    print(f'{piece} -> Composer: {composer}, Key: {key}')

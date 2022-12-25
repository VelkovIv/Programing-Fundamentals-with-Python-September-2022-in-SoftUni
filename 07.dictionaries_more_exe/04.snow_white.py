dwarfs = {}

while True:
    current_dwarf = input().split(' <:> ')

    if current_dwarf[0] == 'Once upon a time':
        break

    name, hat_color, physics = current_dwarf[0], current_dwarf[1], int(current_dwarf[2])

    the_key = '(' + hat_color + ') ' + name

    if the_key not in dwarfs.keys():
        dwarfs[the_key] = 0

    if dwarfs[the_key] > physics:
        continue

    dwarfs[the_key] = physics

for key, physics in sorted(dwarfs.items(), key=lambda x: (-x[1], x[0])):
    print(f'{key} <-> {physics}')

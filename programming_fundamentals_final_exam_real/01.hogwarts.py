def abjuration_func(spell):
    spell = spell.upper()
    print(spell)

    return spell


def necromancy_func(spell):
    spell = spell.lower()
    print(spell)

    return spell


def illusion_func(spell,index,letter):
    if 0 <= index <len(spell):
        spell = spell[:index] + letter + spell[index+1:]
        print('Done!')
    else:
        print('The spell was too weak.')

    return spell


def divination_func(spell, first_substring, second_substring):
    if first_substring in spell:
        spell = spell.replace(first_substring, second_substring)
        print(spell)

    return spell


def alteration_func(spell,substring):
    if substring in spell:
        spell = spell.replace(substring, '')
        print(spell)

    return spell


spell = input()

commands = input().split()
while commands[0] != 'Abracadabra':
    if commands[0] == 'Abjuration':
        spell = abjuration_func(spell)

    elif commands[0] == 'Necromancy':
        spell = necromancy_func(spell)

    elif commands[0] == 'Illusion':
        index, letter = int(commands[1]), commands[2]

        spell = illusion_func(spell,index,letter)

    elif commands[0] == 'Divination':
        first_substring, second_substring = commands[1], commands[2]

        spell = divination_func(spell, first_substring, second_substring)

    elif commands[0] == 'Alteration':
        substring = commands[1]

        spell = alteration_func(spell,substring)

    else:
        print('The spell did not work!')

    commands = input().split()



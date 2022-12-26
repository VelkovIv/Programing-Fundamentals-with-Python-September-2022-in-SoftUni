import re

health_pattern = r'[^0-9\+\-\/\*\.]'
damage_pattern_numbers = r'((\+|\-)?(\d+(\.\d+)?))'
damage_pattern_additional = r'[*\/]'
demons_specs = {}
demons = input().split(',')


for demon in demons:
    demon = demon.strip()

    health = re.findall(health_pattern, demon)
    demon_health = 0

    if health:
        for symbol in health:
            demon_health += ord(symbol)

    if demon not in demons_specs.keys():
        demons_specs[demon] = []
    demons_specs[demon].append(demon_health)

    damage_num = re.findall(damage_pattern_numbers, demon)
    damage_add = re.findall(damage_pattern_additional, demon)
    demon_damage = 0

    if damage_num:
        for num in damage_num:
            demon_damage += float(num[0])

        if damage_add:
            for symbol in damage_add:
                if symbol == '*':
                    demon_damage *= 2
                else:
                    demon_damage /= 2

    if demon not in demons_specs.keys():
        demons_specs[demon] = []
    demons_specs[demon].append(demon_damage)

for demon, specs in sorted(demons_specs.items()):
    print(f'{demon.strip()} - {specs[0]} health, {specs[1]:.2f} damage')

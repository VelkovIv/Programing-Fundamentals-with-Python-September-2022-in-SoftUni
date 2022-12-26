def cast_spell_func(heroes_, name, mp_, spell_):
    if heroes_[name][1] >= mp_:
        heroes_[name][1] -= mp_
        current_mp = heroes_[name][1]
        print(f'{name} has successfully cast {spell_} and now has {current_mp} MP!')
    else:
        print(f'{name} does not have enough MP to cast {spell_}!')

    return heroes_


def take_damage_func(heroes_, name, damage_, attacker_):
    if heroes_[name][0] > damage_:
        heroes_[name][0] -= damage_
        current_hp = heroes_[name][0]
        print(f'{name} was hit for {damage_} HP by {attacker_} and now has {current_hp} HP left!')
    else:
        del heroes_[name]
        print(f'{name} has been killed by {attacker_}!')

    return heroes_


def recharge_func(heroes_, name, amount_):
    if heroes_[name][1] + amount_ > 200:
        recharge = 200 - heroes_[name][1]
        heroes_[name][1] = 200
        print(f'{name} recharged for {recharge} MP!')
    else:
        heroes_[name][1] += amount_
        print(f'{name} recharged for {amount_} MP!')

    return heroes_


def heal_func(heroes_, name, amount_):
    if heroes_[name][0] + amount_ > 100:
        recharge = 100 - heroes_[name][0]
        heroes_[name][0] = 100
        print(f'{name} healed for {recharge} HP!')
    else:
        heroes_[name][0] += amount_
        print(f'{name} healed for {amount_} HP!')

    return heroes_


number_of_heroes = int(input())
heroes = {}

for _ in range(number_of_heroes):
    current_hero = input().split()
    hero, hp, mp = current_hero[0], int(current_hero[1]), int(current_hero[2])

    if hero not in heroes.keys():
        heroes[hero] = [0, 0]
    # Creating a dictionary heroes were hero in key and the value is a list with 2 elements
    # HP (hit points) index 0 and MP (mana points) index 1. HP max = 100 and MP max = 200

    if hp > 100:
        hp = 100
    heroes[hero][0] = hp

    if mp > 200:
        mp = 200
    heroes[hero][1] = mp

while True:
    current_action = input().split(' - ')

    if current_action[0] == 'End':
        break

    hero_name = current_action[1]

    if current_action[0] == 'CastSpell':
        mp_needed, spell = int(current_action[2]), current_action[3]

        heroes = cast_spell_func(heroes, hero_name, mp_needed, spell)

    elif current_action[0] == 'TakeDamage':
        damage, attacker = int(current_action[2]), current_action[3]

        heroes = take_damage_func(heroes, hero_name, damage, attacker)

    elif current_action[0] == 'Recharge':
        amount = int(current_action[2])

        heroes = recharge_func(heroes, hero_name, amount)

    elif current_action[0] == 'Heal':
        amount = int(current_action[2])

        heroes = heal_func(heroes, hero_name, amount)

for hero_name, stat in heroes.items():
    print(f'{hero_name}\n  HP: {stat[0]}\n  MP: {stat[1]}')

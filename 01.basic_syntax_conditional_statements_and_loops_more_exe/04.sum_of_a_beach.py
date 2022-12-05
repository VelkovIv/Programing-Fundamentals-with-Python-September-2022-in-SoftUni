string_to_check = input()

counter = 0

if 'sand' in string_to_check.lower():
    sand = string_to_check.lower().count('sand')
    counter += sand

if 'water' in string_to_check.lower():
    water = string_to_check.lower().count('water')
    counter += water

if 'fish' in string_to_check.lower():
    fish = string_to_check.lower().count('fish')
    counter += fish

if 'sun' in string_to_check.lower():
    sun = string_to_check.lower().count('sun')
    counter += sun

print(counter)

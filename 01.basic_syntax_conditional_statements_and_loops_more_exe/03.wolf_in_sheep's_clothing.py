animals = input().split(', ')
wolf=0
for index in range(-1, -len(animals)-1,-1):
    if animals[index] == 'wolf':
        wolf = abs(index)
if wolf == 1:
    print('Please go away and stop eating my sheep')
else:
    eated_sheep = wolf -1
    print(f'Oi! Sheep number {eated_sheep}! You are about to be eaten by a wolf!')
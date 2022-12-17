number_of_rooms = int(input())
game_on = True
total_free_chairs = 0
for room in range(1, number_of_rooms + 1) :
    chairs_in_the_room, visitors = input().split(' ')
    difference = len(chairs_in_the_room) - int(visitors)
    if difference < 0 :
        print(f'{abs(difference)} more chairs needed in room {room}')
        game_on = False
    else:
        total_free_chairs+=difference
if game_on:
    print(f'Game On, {total_free_chairs} free chairs left')
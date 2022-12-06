number_of_fillings = int(input())
tank_capasity = 255
total_litters = 0
for current_fill in range(number_of_fillings) :
    currrent_litters = int(input())
    if tank_capasity < currrent_litters :
        print('Insufficient capacity!')
        continue
    tank_capasity -= currrent_litters
    total_litters+=currrent_litters
print(total_litters)
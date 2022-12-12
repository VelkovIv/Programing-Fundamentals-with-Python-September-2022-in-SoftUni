all_cars_time = input().split()
one_car_time = len(all_cars_time) // 2
left_car_time = 0
right_car_time = 0
for car_time in range(1,one_car_time+1) :
    current_time_left = int(all_cars_time[car_time-1])
    left_car_time += current_time_left
    if current_time_left == 0:
        left_car_time *=0.8
    current_time_right = int(all_cars_time[-car_time])
    right_car_time += current_time_right
    if current_time_right == 0 :
        right_car_time *= 0.8
if left_car_time < right_car_time:
    print(f'The winner is left with total time: {left_car_time:.1f}')
else:
    print(f'The winner is right with total time: {right_car_time:.1f}')
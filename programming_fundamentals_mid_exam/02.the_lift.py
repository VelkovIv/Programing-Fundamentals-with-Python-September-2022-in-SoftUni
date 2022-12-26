# in Judge 70/100
people_waithing_for_lift = int(input())
lift_status = list(map(int, input().split()))
lift_with_people = []
for cabin in range(len(lift_status)) :
    free_seats = 4 - lift_status[cabin]
    people_waithing_for_lift -= free_seats
    # if lift_status[cabin] != 0 :
    #     free_seats = 4
    if people_waithing_for_lift < 0 :
        free_seats += people_waithing_for_lift
    lift_with_people.append(int(free_seats))
if people_waithing_for_lift > 0 :
    print(f"There isn't enough space! {people_waithing_for_lift} people in a queue!")
    print(*lift_with_people, sep=' ')
elif people_waithing_for_lift < 0 :
    print("The lift has empty spots!")
    print(*lift_with_people, sep=' ')
elif people_waithing_for_lift == 0 :
    print(*lift_with_people, sep=' ')
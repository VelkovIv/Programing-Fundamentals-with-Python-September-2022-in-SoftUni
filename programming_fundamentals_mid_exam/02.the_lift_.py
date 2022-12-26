people_waithing_for_lift = int(input())
lift_status = list(map(int, input().split()))

for cabin in range(len(lift_status)) :
    if lift_status[cabin] == 0 :

        if people_waithing_for_lift < 4 :
            lift_status[cabin] = people_waithing_for_lift
            people_waithing_for_lift = 0
        else :
            lift_status[cabin] = 4
            people_waithing_for_lift -= 4

    else :
        free_seats = 4 - lift_status[cabin]
        lift_status[cabin] += free_seats
        people_waithing_for_lift -= free_seats

if people_waithing_for_lift == 0 :
    print('The lift has empty spots!')
    print(*lift_status, sep=' ')
else :
    print(f"There isn't enough space! {people_waithing_for_lift} people in a queue!")
    print(*lift_status, sep=' ')

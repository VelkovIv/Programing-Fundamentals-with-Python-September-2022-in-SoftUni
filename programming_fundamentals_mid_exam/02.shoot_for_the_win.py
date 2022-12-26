def shooting(targers, current_shoot) :
    shooted_target = 0
    # if targers[current_shoot] > 0 :
    shooted_target = targers[current_shoot]
    targers[current_shoot] = -1
    for target in range(len(targers)) :
        if targers[target] > shooted_target :
            targers[target] -= shooted_target
        elif targers[target] <= shooted_target and targers[target] != -1 :
            targers[target] += shooted_target
    # else :
    #     return targers
    return targers


target_values = list(map(int, input().split(' ')))
while True :
    command = input()
    if command == 'End' :
        break
    shooting_target = int(command)
    if 0 <= shooting_target < len(target_values) and target_values[shooting_target] != -1 :
        result = shooting(target_values, shooting_target)
result_as_str = [str(x) for x in result]
shot_terget_counter = target_values.count(-1)
print(f"Shot targets: {shot_terget_counter} -> {' '.join(result_as_str)}")

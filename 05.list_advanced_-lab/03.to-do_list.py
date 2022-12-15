to_do_list = []
while True :
    command = input()
    if command == 'End' :
        break
    current_element = command.split('-')
    index = int(current_element[0])
    value = current_element[1]
    to_do_list.append([index, value])

sorted_to_do_list = [ element[1] for element in sorted(to_do_list)]
print(sorted_to_do_list)

sequence_of_elements = input().split()
move_counter = 0
win_the_game = False
while True :

    command = input()
    if command == 'end' :
        break

    move_counter += 1
    index1, index2 = command.split(' ')
    index1 = int(index1)
    index2 = int(index2)

    if index1 < 0 or index1 > len(sequence_of_elements) or index2 < 0 or index2 > len(
            sequence_of_elements) or index1 == index2 :
        place = int(len(sequence_of_elements) / 2)
        sequence_of_elements.insert(place, f"-{move_counter}a")
        sequence_of_elements.insert(place, f"-{move_counter}a")
        print('Invalid input! Adding additional elements to the board')
        continue

    if sequence_of_elements[index1] != sequence_of_elements[index2] :
        print('Try again!')
        continue

    if index1 > index2 :
        element = sequence_of_elements.pop(index2)
        sequence_of_elements.pop(index1 - 1)
        print(f'Congrats! You have found matching elements - {element}!')
    else :
        element = sequence_of_elements.pop(index1)
        sequence_of_elements.pop(index2 - 1)
        print(f'Congrats! You have found matching elements - {element}!')

    if len(sequence_of_elements) == 0 :
        win_the_game = True
        break

if win_the_game :
    print(f"You have won in {move_counter} turns!")
else :
    print('Sorry you lose :(')
    print(' '.join(sequence_of_elements))

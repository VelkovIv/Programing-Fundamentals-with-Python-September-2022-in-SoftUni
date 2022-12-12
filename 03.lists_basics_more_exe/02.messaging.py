sequence_of_numbers = input().split()
string_for_message =  input()
sum_counter = 0
string_lenght = len(string_for_message)
for element in range(len(sequence_of_numbers)) :
    number = sequence_of_numbers[element]
    sum = 0
    for digit in number :
        sum += int(digit)
    sum += sum_counter
    if sum > string_lenght :
        sum -= string_lenght
    print(string_for_message[sum :sum + 1], end='')
    sum_counter += 1


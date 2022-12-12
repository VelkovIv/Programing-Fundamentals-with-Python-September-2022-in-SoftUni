sequence_of_numbers = input().split()
string_for_message = input()
char_index_step = 0
massage_indexes = []
massage_to_print = []
for element in range(len(sequence_of_numbers)) :
    number = sequence_of_numbers[element]
    sum = 0
    for digit in number :
        sum += int(digit)
    massage_indexes.append(sum)
for index in range(len(massage_indexes)) :
    char_index = 0
    char_index = (massage_indexes[index] + char_index_step) % len(string_for_message)
    massage_to_print.append(string_for_message[char_index :char_index + 1])
    char_index_step += 1
print(''.join(massage_to_print))

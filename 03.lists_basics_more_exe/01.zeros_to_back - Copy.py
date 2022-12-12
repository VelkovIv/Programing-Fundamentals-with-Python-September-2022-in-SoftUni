list_of_numbers = input().split(', ')
zero_counter = 0
new_numbers_list = []
for index in range(len(list_of_numbers)) :
    if list_of_numbers[index] == '0' :
        zero_counter += 1
    else :
        new_numbers_list.append(int(list_of_numbers[index]))
for zero in range(zero_counter):
    new_numbers_list.append(0)
print(new_numbers_list)

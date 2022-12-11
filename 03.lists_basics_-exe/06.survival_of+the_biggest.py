list_of_numbers = input().split()
number_to_remove = int(input())
for number in range(number_to_remove) :
    min_number = 10000000000000
    for index in range(len(list_of_numbers)-1,-1,-1) :
        if int(min_number) > int(list_of_numbers[index]) :
            min_number = list_of_numbers[index]
    list_of_numbers.remove(min_number)
print(', '.join(list_of_numbers))

list_of_numbers = list(map(int,input().split(' ')))
only_even_numbers = filter(lambda num : num % 2 == 0, list_of_numbers)
print(list(only_even_numbers))


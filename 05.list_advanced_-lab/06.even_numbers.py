numbers = list(map(int, input().split(', ')))
indexes_of_even_numbers = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
print(indexes_of_even_numbers)

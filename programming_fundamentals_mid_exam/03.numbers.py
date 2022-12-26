numbers = list(map(int, input().split(' ')))

average_of_numbers = sum(numbers) / len(numbers)
numbers_above_average = [numbers[number] for number in range(len(numbers)) if numbers[number] > average_of_numbers]
numbers_above_average.sort(reverse=True)
to5_5_numbers_above_average = numbers_above_average[:5]

if len(to5_5_numbers_above_average) == 0:
  print('No')
else:
 print(*to5_5_numbers_above_average, sep=' ')

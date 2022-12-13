numbers = list(map(float, input().split(' ')))
abs_numbers = []
for number in numbers:
    abs_numbers.append(abs(number))

print(abs_numbers)

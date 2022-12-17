def positive_numbers(list_of_numbers) :
    positive_numbers = []
    for number in list_of_numbers :
        if int(number) >= 0 :
            positive_numbers.append(number)
    return positive_numbers


def negative_numbers(list_of_numbers) :
    negative_numbers = []
    for number in list_of_numbers :
        if int(number) < 0 :
            negative_numbers.append(number)
    return negative_numbers


def even_numbers(list_of_numbers) :
    even_numbers = []
    for number in list_of_numbers :
        if int(number) % 2 == 0 :
            even_numbers.append(number)
    return even_numbers


def odd_numbers(list_of_numbers) :
    odd_numbers = []
    for number in list_of_numbers :
        if int(number) % 2 != 0 :
            odd_numbers.append(number)
    return odd_numbers


numbers = input().split(', ')
print(f'Positive: {", ".join(positive_numbers(numbers))}')
print(f'Negative: {", ".join(negative_numbers(numbers))}')
print(f'Even: {", ".join(even_numbers(numbers))}')
print(f'Odd: {", ".join(odd_numbers(numbers))}')

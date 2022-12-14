def sum_numbers(number1, number2) :
    return number1 + number2


def subtract(first, second) :
    return first - second


def add_and_subtract(num1, num2, num3) :
    sum = sum_numbers(num1, num2)
    result = subtract(sum, num3)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))

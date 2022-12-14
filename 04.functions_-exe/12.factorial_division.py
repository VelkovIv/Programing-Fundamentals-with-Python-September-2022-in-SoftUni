def factorial(num) :
    for number in range(1, num):
        num *= number
    return num


first_number = int(input())
second_number = int(input())
result = factorial(first_number) / factorial(second_number)
print(f'{result:.2f}')

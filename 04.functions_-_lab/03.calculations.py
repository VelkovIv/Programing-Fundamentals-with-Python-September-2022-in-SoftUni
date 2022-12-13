def calculation(first_number, second_number, operation) :
    if operation == 'multiply' :
        return first_number * second_number
    elif operation == 'divide' :
        return int(first_number / second_number)
    elif operation == 'add':
        return first_number + second_number
    elif operation == 'subtract':
        return first_number - second_number


operation = input()
first_number = int(input())
second_number = int(input())

print(calculation(first_number,second_number,operation))

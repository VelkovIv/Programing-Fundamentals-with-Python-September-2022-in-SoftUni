def sum_odd_and_even_number(number) :
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in str(number) :
        digit=int(digit)
        if digit % 2 == 0 :
            sum_of_even_digits += digit
        else :
            sum_of_odd_digits += digit

    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


number = int(input())
print(sum_odd_and_even_number(number))

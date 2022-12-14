def check_perfrct_num(number) :
    sum = 0
    for divisor in range(1, (number // 2) + 1) :
        if number % divisor == 0 :
            sum += divisor
    if sum == number :
        return 'We have a perfect number!'
    else :
        return "It's not so perfect."


number = int(input())
result = check_perfrct_num(number)
print(result)

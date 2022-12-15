def tribonachi_siquence(num) :
    tribonachi_list = []
    sum = 0
    for number in range(1, num + 1) :
        if number == 1 or number == 2 :
            tribonachi_list.append(1)
        elif number == 3 :
            tribonachi_list.append(2)
        else :
            sum = tribonachi_list[-3] + tribonachi_list[-2] + tribonachi_list[-1]
            tribonachi_list.append(sum)
    return tribonachi_list

number = int(input())
print(*tribonachi_siquence(number), sep=' ')

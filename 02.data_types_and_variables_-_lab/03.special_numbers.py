number = int(input())

for current_number in range(1, number + 1) :
    digit_sum = 0
    digit_sum += current_number % 10 + int(current_number / 10)
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11 :
        print(f'{current_number} -> True')
    else :
        print(f'{current_number} -> False')

# i= int(input())
# d = 10
# d= d^(len(str(i))-1)
# s = 0
# s1 = i % d
# s2 = int(i/d)
# s= s1 + s2
# print(len(str(i))-1)
# print(d)
# print(s1)
# print(s2)
# print(s)

def smallest_num(num):
    min_number = min(num)
    return min_number


first_number = int(input())
second_number = int(input())
third_number = int(input())
number_list=[first_number, second_number, third_number]

print(smallest_num(number_list))
def min_num(nums) :
    min_num = min(nums)
    return f"The minimum number is {min_num}"


def max_num(nums) :
    max_num = max(nums)
    return f"The maximum number is {max_num}"


def sum_of_numbers(nums) :
    sum = 0
    for number in range(len(nums)) :
        sum += int(nums[number])
    return f"The sum number is: {sum}"


list_of_number = list(map(int, input().split(' ')))
print(min_num(list_of_number))
print(max_num(list_of_number))
print(sum_of_numbers(list_of_number))

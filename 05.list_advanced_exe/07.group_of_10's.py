def list_of_numbers(numbers, group) :
    return [number for number in numbers if number > group - 10 and number <= group]


siquence_of_numbers = list(map(int, input().split(', ')))
max_number = max(siquence_of_numbers)
for current_group in range(10, max_number + 10, 10) :
    print(f"Group of {current_group}'s: {list_of_numbers(siquence_of_numbers, current_group)}")

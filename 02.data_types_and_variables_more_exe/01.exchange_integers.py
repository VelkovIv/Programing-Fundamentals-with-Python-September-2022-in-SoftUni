number_one = int(input())
number_two = int(input())
print('Before:')
print(f'a = {number_one}')
print(f'b = {number_two}')
temp_one = number_one
number_one = number_two
number_two = temp_one
print('After:')
print(f'a = {number_one}')
print(f'b = {number_two}')

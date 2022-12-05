number_of_chairs = int(input())
total_sum = 0
for chairs in range(number_of_chairs):
    current_chair = input()
    total_sum +=ord(current_chair)
print(f'The sum equals: {total_sum}')
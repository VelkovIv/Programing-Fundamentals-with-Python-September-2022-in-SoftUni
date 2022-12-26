from math import ceil

employee_one_efficiency_per_hour = int(input())
employee_two_efficiency_per_hour = int(input())
employee_three_efficiency_per_hour = int(input())
number_of_students = int(input())

answers_capasity_per_hour = employee_one_efficiency_per_hour + \
                            employee_two_efficiency_per_hour + employee_three_efficiency_per_hour
needed_time = ceil(number_of_students / answers_capasity_per_hour)
total_time = 0
while needed_time != 0 :
    if needed_time < 4 :
        total_time += needed_time
        break
    needed_time -= 3
    total_time += 4

print(f'Time needed: {total_time}h.')

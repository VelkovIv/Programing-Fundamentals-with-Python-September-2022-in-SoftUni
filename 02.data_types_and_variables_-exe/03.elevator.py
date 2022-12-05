from math import ceil

number_of_people = int(input())
evevator_capacity = int(input())
evevator_courses = ceil(number_of_people / evevator_capacity)
print(evevator_courses)
employees_happiness = list(map(int, input().split(' ')))
happiness_factor = int(input())
total_happiness = [employee * happiness_factor for employee in employees_happiness]
the_happy = list(filter(lambda h : h >= sum(total_happiness) / len(total_happiness), total_happiness))

if len(the_happy) >= len(total_happiness) / 2 :
    print(f'Score: {len(the_happy)}/{len(total_happiness)}. Employees are happy!')
else :
    print(f'Score: {len(the_happy)}/{len(total_happiness)}. Employees are not happy!')

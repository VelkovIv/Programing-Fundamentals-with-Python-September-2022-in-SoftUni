number_of_student = int(input())
number_of_lectures = int(input())
aditional_bonus = int(input())

bonuses = []
max_lecture_atendence = 0

for student in range(number_of_student) :
    student_atendences = int(input())

    bonus = student_atendences / number_of_lectures * (5 + aditional_bonus)
    bonuses.append(bonus)

    if max_lecture_atendence <= student_atendences :
        max_lecture_atendence = student_atendences


print(f'Max Bonus: {round(max(bonuses))}.')
print(f'The student has attended {max_lecture_atendence} lectures.')
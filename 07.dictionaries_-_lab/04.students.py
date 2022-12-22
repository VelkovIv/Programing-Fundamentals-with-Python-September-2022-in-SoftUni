command = input().split(':')
students = {}
while len(command) > 1 :
    name, id, course = command[0], command[1], command[2]

    if course not in students.keys() :
        students[course] = []

    students[course].append(f'{name} - {id}')

    command = input().split(':')

seached_course = command[0].replace('_', ' ')

for course in students[seached_course] :
    print(course)

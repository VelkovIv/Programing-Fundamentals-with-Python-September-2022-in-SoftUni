___doc___ = """
Write a program that keeps the information about students and their grades. 
On the first line, you will receive an integer number representing the next pair of rows.
On the next lines, you will be receiving each student's name and their grade. 
Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
Print the final dictionary with students and their average grade in the following format:
"{name} -> {averageGrade}"
Format the average grade to the 2nd decimal place.

---------------------------------------------------------
Examples
---------------------------------------------------------
--->Input
5
John
5.5
John
4.5
Alice
6
Alice
3
George
5

Output--->
hn -> 5.00
Alice -> 4.50
George -> 5.00

---------------------------------------------------------
--->Input
5
Amanda
3.5
Amanda
4
Rob
5.5
Christian
5
Robert
6

Output--->
Rob -> 5.50
Christian -> 5.00
Robert -> 6.00

---------------------------------------------------------
"""

number_of_students = int(input())

all_students_and_ave_grades = {}
best_students = {}

for student in range(number_of_students) :
    student_name = input()
    student_grade = float(input())

    if student_name not in all_students_and_ave_grades.keys() :
        all_students_and_ave_grades[student_name] = student_grade
    else :
        new_grade = (student_grade + all_students_and_ave_grades[student_name]) / 2
        all_students_and_ave_grades[student_name] = new_grade

for student,grade in all_students_and_ave_grades.items():
    if all_students_and_ave_grades[student] < 4.5 :
        continue
    best_students[student] = grade


for name, average_grade in best_students.items():
    print(f"{name} -> {average_grade:.2f}")
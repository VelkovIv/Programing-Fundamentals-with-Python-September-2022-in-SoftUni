___doc___ = """
Write a program that keeps the information about courses. Each course has a name and registered students.
You will be receiving a course name and a student name until you receive the command "end". 
You should register each user into the corresponding course. If the given course does not exist, add it. 
When you receive the command "end", print the courses with their names and total registered users.
For each course, print the registered users.
Input
•	Until the "end" command is received, you will be receiving input lines in the format: 
"{course_name} : {student_name}"
•	The product data is always delimited by " : "
Output
•	Print the information about each course in the following format: 
"{course_name}: {registered_students}"
•	Print the information about each student in the following format:
"-- {student_name}"
---------------------------------------------------------
Examples
---------------------------------------------------------
--->Input
Programming Fundamentals : John Smith
Programming Fundamentals : Linda Johnson
JS Core : Will Wilson
Java Advanced : Harrison White
end

Output--->
Programming Fundamentals: 2
-- John Smith
-- Linda Johnson
JS Core: 1
-- Will Wilson
Java Advanced: 1
-- Harrison White

---------------------------------------------------------
--->Input
Algorithms : Jay Moore
Programming Basics : Martin Taylor
Python Fundamentals : John Anderson
Python Fundamentals : Andrew Robinson
Algorithms : Bob Jackson
Python Fundamentals : Clark Lewis
end

Output--->
Algorithms: 2
-- Jay Moore
-- Bob Jackson
Programming Basics: 1
-- Martin Taylor
Python Fundamentals: 3
-- John Anderson
-- Andrew Robinson
-- Clark Lewis

---------------------------------------------------------
"""

courses = {}

while True :

    current_course = input().split(" : ")

    if current_course[0] == 'end' :
        break

    course_name, student_name = current_course

    if course_name not in courses.keys() :
        courses[course_name] = []

    courses[course_name].append(student_name)

for course_name, registered_students in courses.items() :
    print(f"{course_name}: {len(registered_students)}")

    for student_name in registered_students :
        print(f"-- {student_name}")

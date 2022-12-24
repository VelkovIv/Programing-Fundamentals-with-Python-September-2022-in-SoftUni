___doc___ = """
Write a program that keeps the information about companies and their employees. 
You will be receiving company names and an employees' id until you receive the command "End" command.
Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
Print the company name and each employee's id in the following format:
"{company_name}
-- {id1}
-- {id2}
…
-- {idN}"
Input / Constraints
•	Until you receive the "End" command, you will be receiving input in the format: 
"{company_name} -> {employee_id}".
•	The input always will be valid.

---------------------------------------------------------
Examples
---------------------------------------------------------
--->Input
SoftUni -> AA12345
SoftUni -> BB12345
Microsoft -> CC12345
HP -> BB12345
End

Output--->
SoftUni
-- AA12345
-- BB12345
Microsoft
-- CC12345
HP
-- BB12345

---------------------------------------------------------
--->Input
SoftUni -> AA12345
SoftUni -> CC12344
Lenovo -> XX23456
SoftUni -> AA12345
Movement -> DD11111
End

Output--->
SoftUni
-- AA12345
-- CC12344
Lenovo
-- XX23456
Movement
-- DD11111

---------------------------------------------------------
"""

company_users = {}

while True:
    current_input = input()

    if current_input == 'End':
        break

    current_company, current_user = current_input.split(' -> ')

    if current_company not in company_users.keys():
        company_users[current_company]=[]

    if current_user not in company_users[current_company]  :
        company_users[current_company].append(current_user)

for company_name, current_id in company_users.items():
    print(f'{company_name}')
    for id in current_id:
        print(f'-- {id}')
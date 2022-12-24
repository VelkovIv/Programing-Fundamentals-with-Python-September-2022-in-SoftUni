___doc___ = """
SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work.
It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
The program receives 2 types of commands:
•	"register {username} {license_plate_number}":
o	The system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print:
"ERROR: already registered with plate number {license_plate_number}"
o	If the check above passes successfully, the user should be registered, so the system should print:
 "{username} registered {license_plate_number} successfully"
•	"unregister {username}":
o	If the user is not present in the database, the system should print:
"ERROR: user {username} not found"
o	If the check above passes successfully, the system should print:
"{username} unregistered successfully"
After you execute all of the commands, print all the currently registered users and their license plates in the format: 
•	"{username} => {license_plate_number}"
Input
•	First line: n - number of commands - integer
•	Next n lines: commands in one of the two possible formats:
o	Register: "register {username} {license_plate_number}"
o	Unregister: "unregister {username}"
The input will always be valid, and you do not need to check it explicitly.

--------------------------------------------------
Examples
--------------------------------------------------
--->Input
5
register John CS1234JS
register George JAVA123S
register Andy AB4142CD
register Jesica VR1223EE
unregister Andy

Output--->
John registered CS1234JS successfully
George registered JAVA123S successfully
Andy registered AB4142CD successfully
Jesica registered VR1223EE successfully
Andy unregistered successfully
John => CS1234JS
George => JAVA123S
Jesica => VR1223EE

---------------------------------------------------
--->Input
4
register Jony AA4132BB
register Jony AA4132BB
register Linda AA9999BB
unregister Jony

Output--->
Jony registered AA4132BB successfully
ERROR: already registered with plate number AA4132BB
Linda registered AA9999BB successfully
Jony unregistered successfully
Linda => AA9999BB

--------------------------------------------------
--->Input
register Jacob MM1111XX
register Anthony AB1111XX
unregister Jacob
register Joshua DD1111XX
unregister Lily
register Samantha AA9999BB

Output--->
Jacob registered MM1111XX successfully
Anthony registered AB1111XX successfully
Jacob unregistered successfully
Joshua registered DD1111XX successfully
ERROR: user Lily not found
Samantha registered AA9999BB successfully
Anthony => AB1111XX
Joshua => DD1111XX
Samantha => AA9999BB

"""

number_of_commands = int(input())
regisred_cars = {}

for car in range(number_of_commands) :
    current_command = input().split()

    if current_command[0] == 'register' :
        action, user_name, license_plate_number = current_command

        if user_name not in regisred_cars:
            regisred_cars[user_name]= license_plate_number
            print(f"{user_name} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")


    elif current_command[0] == 'unregister' :
        action, user_name = current_command
        if user_name not in regisred_cars:
            print(f"ERROR: user {user_name} not found")
        else:
            del regisred_cars[user_name]
            print(f"{user_name} unregistered successfully")

for username,license_plate_number in regisred_cars.items():
    print(f"{username} => {license_plate_number}")
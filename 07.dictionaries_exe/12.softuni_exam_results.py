___doc___ = """
Judge statistics on the last Programing Fundamentals exam were not working correctly, 
so you have the task of taking all the submissions and analyzing them properly. 
You should collect all the submissions and print the final results and statistics about each language 
in which the participants submitted their solutions.
You will be receiving lines in the following format: "{username}-{language}-{points}" 
until you receive "exam finished". You should store each username and their submissions and points. 
If a student has two or more submissions for the same language, save only his maximum points.
You can receive a command to ban a user for cheating in the following format: "{username}-banned". 
In that case, you should remove the user from the contest but preserve his submissions in the total count 
of submissions for each language.
After receiving "exam finished", print each of the participants in the following format:
"Results:
{username1} | {points}
{username2} | {points}
…
{usernameN} | {points}"
After that, print each language used in the exam in the following format:
"Submissions:
{language1} - {submissions_count}
{language2} - {submissions_count}
…
{language3} - {submissions_count}"
Input / Constraints
Until you receive "exam finished" you will be receiving participant submissions in the following format: "{username}-{language}-{points}"
You can receive a ban command -> "{username}-banned"
The points of the participant will always be a valid integer in the range [0-100];
Output
•	Print the exam results for each participant
•	After that, print each language in the format shown above
•	Allowed working time / memory: 100ms / 16MB

---------------------------------------------------------
Examples
---------------------------------------------------------
--->Input
Peter-Java-84
George-C#-84
George-C#-70
Katy-C#-94
exam finished

Output--->
Results:
Peter | 84
George | 84
Katy | 94
Submissions:
Java - 1
C# - 3

---------------------------------------------------------
--->Input
Peter-Java-91
George-C#-84
Katy-Java-90
Katy-C#-50
Katy-banned
exam finished

Output--->
Results:
Peter | 91
George | 84
Submissions:
Java - 2
C# - 2

---------------------------------------------------------
"""

exam_results = {}
used_languages = {}

while True :
    command = input()

    if command == 'exam finished' :
        break

    current_command = command.split('-')

    if current_command[1] == 'banned' :
        exam_results[current_command[0]] = "banned"

    else :
        username, language, points = current_command
        if language not in used_languages.keys() :
            used_languages[language] = 0
        used_languages[language] += 1

        if username not in exam_results.keys() :
            exam_results[username] = int(points)

        else :
            if exam_results[username] < int(points) :
                exam_results[username] = int(points)

print("Results:")
for username, points in exam_results.items() :
    if points != 'banned' :
        print(f'{username} | {points}')
print("Submissions:")
for language, submissions_count in used_languages.items() :
    print(f'{language} - {submissions_count}')

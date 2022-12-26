___doc___ = """
Write a program that processes information about a race. 
On the first line you will be given list of participants separated by ", ". 
On the next few lines until you receive a line "end of race" you will be given some info 
which will be some alphanumeric characters. In between them you could have some extra characters 
which you should ignore. For example: "G!32e%o7r#32g$235@!2e". 
The letters are the name of the person and the sum of the digits is the distance he ran. 
So here we have George who ran 29 km. Store the information about the person only 
if the list of racers contains the name of the person. 
If you receive the same person more than once just add the distance to his old distance. 
At the end print the top 3 racers ordered by distance in descending in the format:
"1st place: {first racer}
2nd place: {second racer}
3rd place: {third racer}"


---------------------------------------------------
Examples
---------------------------------------------------
--->Input
George, Peter, Bill, Tom
G4e@55or%6g6!68e!!@
R1@!3a$y4456@
B5@i@#123ll
G@e54o$r6ge#
7P%et^#e5346r
T$o553m&6
end of race

Output--->
1st place: George
2nd place: Peter
3rd place: Tom

---------------------------------------------------

"""

import re

list_of_perticipiences = input().split(', ')

pattern_names = r'(?i)[a-z]+'
pattern_distance = r'\d'
command = input()
race = {}

while command != 'end of race':
    name = re.findall(pattern_names, command)

    current_name = ''
    current_distance = 0
    for letter in name:
        current_name += letter

    if current_name in list_of_perticipiences:
        distance = re.findall(pattern_distance, command)
        current_distance = [int(num) for num in distance]

        if current_name in race.keys():
            race[current_name] += sum(current_distance)
        else:
            race[current_name] = sum(current_distance)

    command = input()

sorted_race = dict(sorted(race.items(), key=lambda x: x[1], reverse=True))
sorted_race_list = list(sorted_race)

print(f'1st place: {sorted_race_list[0]}')
print(f'2nd place: {sorted_race_list[1]}')
print(f'3rd place: {sorted_race_list[2]}')

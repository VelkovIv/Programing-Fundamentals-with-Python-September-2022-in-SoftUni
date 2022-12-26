___doc___ = """
The war is in its peak, but you, young Padawan, can turn the tides with your programming skills. 
You are tasked to create a program to decrypt the messages of The Order and prevent the death of hundreds of lives. 
You will receive several messages, which are encrypted using the legendary star enigma. You should decrypt the messages,
following these rules:
To properly decrypt a message, you should count all the letters [s, t, a, r] – case insensitive and 
remove the count from the current ASCII value of each symbol of the encrypted message.
After decryption:
Each message should have a planet name, population, attack type ('A', as attack or 'D', as destruction)
and soldier count.
The planet name starts after '@' and contains only letters from the Latin alphabet. 
The planet population starts after ':' and is an Integer;
The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
The soldier count starts after "->" and should be an Integer.
The order in the message should be: planet name -> planet population -> attack type -> soldier count. 
Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
Input / Constraints
•	The first line holds n – the number of messages– integer in range [1…100];
•	On the next n lines, you will be receiving encrypted messages.
Output
After decrypting all messages, you should print the decrypted information in the following format:
First print the attacked planets, then the destroyed planets.
"Attacked planets: {attackedPlanetsCount}"
"-> {planetName}"
"Destroyed planets: {destroyedPlanetsCount}"
"-> {planetName}"
The planets should be ordered by name alphabetically.


---------------------------------------------------
Examples
---------------------------------------------------
--->Input
2
STCDoghudd4=63333$D$0A53333
EHfsytsnhf?8555&I&2C9555SR

Output--->
Attacked planets: 1
-> Alderaa
Destroyed planets: 1
-> Cantonica

---------------------------------------------------
--->Input
3
tt(''DGsvywgerx>6444444444%H%1B9444
GQhrr|A977777(H(TTTT
EHfsytsnhf?8555&I&2C9555SR

Output--->
Attacked planets: 0
Destroyed planets: 2
-> Cantonica
-> Coruscant

---------------------------------------------------
"""

import re

pattern = r'(?i)[star]'

pattern_decripted = r'@([A-za-z]+)[^@\-\!\:\>]*:(\d+)[^@\-\!\:\>]*!([AD])[^@\-\!\:\>]*![^@\-\!\:\>]*\->(\d+)'
number_of_massages = int(input())
attacked_planets = []
destroyed_planets = []

for message in range(number_of_massages):
    current_message = input()
    shit = re.findall(pattern, current_message)
    current_shift = len(shit)
    new_massage = current_message.split()
    decripted_massage = ''

    for symbol in current_message:
        decripted_massage += (chr(ord(symbol) - current_shift))
    final_massage = re.search(pattern_decripted, decripted_massage)
    if final_massage:
        planent, population, type, solders = final_massage.groups()

        if type == 'A':
            attacked_planets.append(planent)
        elif type == 'D':
            destroyed_planets.append(planent)

print(f'Attacked planets: {len(attacked_planets)}')
for planet in attacked_planets:
    print(f'-> {planet}')
print(f'Destroyed planets: {len(destroyed_planets)}')
for planet in sorted(destroyed_planets):
    print(f'-> {planet}')

# PQ@Alderaa1:30000!A!->20000
# @Cantonica:3000!D!->4000NM
# pp$##@Coruscant:2000000000!D!->5000
# @Jakku:200000!A!MMMM
# @Cantonica:3000!D!->4000NM
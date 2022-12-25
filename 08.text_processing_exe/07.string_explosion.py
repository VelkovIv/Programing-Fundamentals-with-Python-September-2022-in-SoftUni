___doc___ = """
Write a program that reads a string from the console that contains:
•	Explosions marked with '>'
•	Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
•	Any other characters
Your task is to delete x characters, starting after the exploded character ('>'). 
If you find another explosion mark ('>') while deleting characters, you should add the strength to your previous 
explosion. You should not delete the explosion character – '>'.
When all characters are processed, print the final string. 
Constraints
•	You will always receive strength for the explosions
•	The path will consist only of letters from the Latin alphabet, integers, and the char '>'
•	The strength of the punches will be in the interval [0…9]


---------------------------------------------------
Examples
---------------------------------------------------
--->Input
abv>1>1>2>2asdasd
Output--->
abv>>>>dasd
---------------------------------------------------
--->Input
pesho>2sis>1a>2akarate>4hexmaster
Output--->
pesho>is>a>karate>master
---------------------------------------------------
"""

input_string = input()

final_string = ''
explosion_strength = 0

for index in range(len(input_string)):
    if input_string[index] != '>' and explosion_strength > 0:
        explosion_strength -= 1

    elif input_string[index] == '>':
        final_string += input_string[index]
        explosion_strength += int(input_string[index + 1])

    else:
        final_string += input_string[index]

print(final_string)

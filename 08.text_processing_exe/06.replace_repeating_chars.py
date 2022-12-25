___doc___ = """
Write a program that reads a string from the console and replaces any sequence of the same letters with a single 
corresponding letter.

---------------------------------------------------
Examples
---------------------------------------------------
--->Input
aaaaabbbbbcdddeeeedssaa
Output--->
abcdedsa
---------------------------------------------------
--->Input
qqqwerqwecccwd
Output--->
qwerqwecwd
---------------------------------------------------
"""

input_string = input()
current_character = ''
final_string = ''

for character in input_string:
    if character != current_character:
        current_character = character
        final_string +=character

print(final_string)
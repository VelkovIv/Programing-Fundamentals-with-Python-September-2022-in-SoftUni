___doc___ = """
Write a program that receives a single string. On the first line, print all the digits found in the string, 
on the second – all the letters, and on the third – all the other characters. 
There will always be at least one digit, one letter, and one other character.

---------------------------------------------------
Examples
---------------------------------------------------
--->Input
Agd#53Dfg^&4F53
Output--->
53453
AgdDfgF
#^&
---------------------------------------------------

"""

text = input()

numbers, characters, others = [], [], []

for char in text :
    if char.isnumeric() :
        numbers.append(char)
    elif char.isalpha() :
        characters.append(char)
    else :
        others.append(char)

print(''.join(numbers))
print(''.join(characters))
print(''.join(others))
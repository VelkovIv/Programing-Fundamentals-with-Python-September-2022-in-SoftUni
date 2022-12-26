___doc___ = """
On the first line, you will receive a string. On the second line, you will receive a second string. 
Write a program that removes all the occurrences of the first string in the second until there is no match. 
At the end, print the remaining string.

---------------------------------------------------
Examples
---------------------------------------------------
--->Input
ice
kicegiciceeb

Output--->
kgb
---------------------------------------------------
"""

string_to_remove = input()
word = input()

while string_to_remove in word:
    word = word.replace(string_to_remove,'')

print(word)
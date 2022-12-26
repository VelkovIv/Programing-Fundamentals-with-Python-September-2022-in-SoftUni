___doc___ = """
Write a program that reads a sequence of strings, separated by a single space.
Each string should be repeated N times, where N is the length of the string. 
Print the final strings concatenated into one string.
---------------------------------------------------
Examples
---------------------------------------------------
--->Input
hi abc add
Output--->
hihiabcabcabcaddaddadd
---------------------------------------------------
--->Input
work
Output--->
workworkworkwork
---------------------------------------------------
--->Input
ball
Output--->
ballballballball
---------------------------------------------------
"""

strings = input().split()

for string in strings:
    print(string * len(string), end='')
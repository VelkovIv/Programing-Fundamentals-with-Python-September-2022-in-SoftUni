___doc___ = """
Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
The input will be provided as a single string.


---------------------------------------------------
Examples
---------------------------------------------------
--->Input
There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)
Output--->
:P
:O
:)
---------------------------------------------------
"""

massage = input()

for index in range(len(massage)):
    if massage[index] == ':':
        emoticone = massage[index] + massage[index+1]
        print(emoticone)
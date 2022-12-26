___doc___ = """
Write a program that finds how many times a word is used in a string. 
The output is a single number indicating the number of times the string contains the word. 
Note that letter case does not matter – it is case-insensitive.

---------------------------------------------------
Examples
---------------------------------------------------
--->Input
The waterfall was so high, that the child couldn't see its peak.
the

Output--->
2
---------------------------------------------------
--->Input
How do you plan on achieving that? How? How can you even think of that? 
how

Output--->
3
---------------------------------------------------
--->Input
There was one. Therefore I bought it. I wouldn't buy it otherwise.
there

Output--->
1
---------------------------------------------------
"""

import re

current_string = input()
word = input()
pattern = fr'(?i){word}\b'

repeating_word = re.findall(pattern, current_string)

print(len(repeating_word))

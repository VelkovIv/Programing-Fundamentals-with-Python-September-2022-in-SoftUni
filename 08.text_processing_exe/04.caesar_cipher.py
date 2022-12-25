___doc___ = """
Write a program that returns an encrypted version of the same text. 
Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII table.
For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.

---------------------------------------------------
Examples
---------------------------------------------------
--->Input
Programming is cool!
Output--->
Surjudpplqj#lv#frro$

---------------------------------------------------
--->Input
One year has 365 days.
Output--->
Rqh#|hdu#kdv#698#gd|v1
---------------------------------------------------
"""

def encripted_massage(massage):
    encripted_massage = ""
    for charecter in massage:
        encripted_massage += chr(ord(charecter) + 3)

    return encripted_massage

massage = input()

print(encripted_massage(massage))

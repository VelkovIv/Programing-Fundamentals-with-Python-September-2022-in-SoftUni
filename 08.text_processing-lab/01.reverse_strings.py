___doc___ = """
You will be given strings on separate lines until you receive an "end" command. 
Write a program that reverses strings and prints each pair on a separate line in the format "{word} = {reversed_word}".

---------------------------------------------------
Examples
---------------------------------------------------
--->Input
helLo
Softuni
bottle
end

Output--->
helLo = oLleh
Softuni = inutfoS
bottle = elttob

---------------------------------------------------
--->Input
Dog
caT
chAir
end

Output--->
Dog = goD
caT = Tac
chAir = riAhc

---------------------------------------------------
"""

while True:
    text = input()

    if text == 'end':
        break

    print(f"{text} = {text[::-1]}")

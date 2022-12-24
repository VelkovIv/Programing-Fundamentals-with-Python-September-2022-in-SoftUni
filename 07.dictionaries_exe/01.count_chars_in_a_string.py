___doc___ = """
Write a program that counts all characters in a string except for space (" "). 
Print all the occurrences in the following format:
"{char} -> {occurrences}"

Input	        Output
text            t -> 2
                e -> 1
                x -> 1

text text text  t -> 6
                e -> 3
                x -> 3

"""
text = input().split()
charecters = {}
for i in range(len(text)) :
    for character in text[i] :

        if character not in charecters.keys() :
            charecters[character] = 0
        charecters[character] += 1

for char, occurrences in charecters.items():
    print(f"{char} -> {occurrences}")
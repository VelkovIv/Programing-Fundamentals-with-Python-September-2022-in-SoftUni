__doc__ = """
Write a program that prints all elements from a given sequence of words that occur an odd number of times (case-insensitive) in it.
•	Words are given on a single line, space-separated.
•	Print the result elements in lowercase, in their order of appearance.
Examples
Input	                            Output
Java C# PHP PHP JAVA C java	        java c# c
3 5 5 hi pi HO Hi 5 ho 3 hi pi      5 hi
a a A SQL xx a xx a A a XX c        a sql xx c

"""
words = input().split(" ")
dictonary = {}

for word in words:
    word_lower = word.lower()

    if word_lower not in dictonary:
        dictonary[word_lower] = 0
    dictonary[word_lower] += 1

for key, value in dictonary.items():
    if value % 2 != 0:
        print(key, end=" ")
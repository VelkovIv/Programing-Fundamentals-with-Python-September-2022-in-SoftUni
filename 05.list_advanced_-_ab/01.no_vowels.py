text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
no_vowels = [letter for letter in text if letter.lower() not in vowels]
print(''.join(no_vowels))
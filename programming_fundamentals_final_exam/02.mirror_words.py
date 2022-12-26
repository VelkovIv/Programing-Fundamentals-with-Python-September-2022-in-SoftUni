import re

pattern = r'(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'
test_string = input()

mirror_words = []

words = re.findall(pattern, test_string)

for word in words:
    if word[1] == word[2][::-1]:
        mirror_words.append(word[1] + ' <=> ' + word[2])

if len(words) == 0:
    print('No word pairs found!')
    print('No mirror words!')
else:
    print(f'{len(words)} word pairs found!')
    if len(mirror_words) == 0:
        print('No mirror words!')
    else:
        print(f"The mirror words are:\n{', '.join(mirror_words)}")

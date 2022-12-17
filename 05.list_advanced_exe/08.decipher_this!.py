sectert_massage = input().split(" ")
decoded_massage = []
for word in sectert_massage :
    chair_code = ''
    text_part = ''
    while not word.isalpha() :
        chair_code += word[0 :1]
        word = word[1 :]
    new_word = list(word)
    new_word[0], new_word[-1]=new_word[-1],new_word[0]
    word = ''.join(new_word)
    text_part = word
    letter = chr(int(chair_code))
    decoded_massage.append(letter + text_part)
print(' '.join(decoded_massage))

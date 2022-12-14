def character_in_range(char1, char2) :
    result_list =[]
    for character in range(ord(char1)+1, ord(char2)):
        current_charecter = result_list.append(chr(character))
    return result_list


character_one = input()
character_two = input()
print(' '.join(character_in_range(character_one, character_two)))

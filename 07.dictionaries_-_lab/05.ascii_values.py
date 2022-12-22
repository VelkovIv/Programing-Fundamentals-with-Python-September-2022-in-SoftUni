list_of_character = input().split(', ')

characters = {key:ord(key) for key in list_of_character}

print(characters)

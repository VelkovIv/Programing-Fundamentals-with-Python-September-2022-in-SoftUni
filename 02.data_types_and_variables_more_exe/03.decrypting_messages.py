key=int(input())
numbers_of_character = int(input())
for character in range(numbers_of_character):
    temp_value = 0
    current_character = input()
    temp_value = key + ord(current_character)
    print(f'{chr(temp_value)}',end='')
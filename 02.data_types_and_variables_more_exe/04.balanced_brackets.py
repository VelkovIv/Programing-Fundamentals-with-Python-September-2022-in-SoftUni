iterations = int(input())
open_bracket_counter = 0
is_open = False
is_balanced = False
close_bracket_counter = 0
for iteration in range(iterations) :
    current_input = input()
    if current_input == "(" or current_input == " (" or current_input == "( " or current_input == " ( " :
        open_bracket_counter += 1
        if open_bracket_counter - close_bracket_counter == 2 :
            is_balanced = False
            break
        is_open = True
    if current_input == ")" or current_input == " )" or current_input == ") " or current_input == " ) " :
        close_bracket_counter += 1
        if is_open :
            is_open = False
            is_balanced = True
if is_balanced and open_bracket_counter == close_bracket_counter :
    print('BALANCED')
else :
    print('UNBALANCED')

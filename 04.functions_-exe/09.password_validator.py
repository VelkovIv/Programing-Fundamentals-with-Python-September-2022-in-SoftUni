def lenght_check(password) :
    if len(password) < 6 or len(password) > 10 :
        return False


def letter_and_digit_check(password) :
    if not password.isalnum() :
        return False


def minimum_digit_check(password) :
    digit_counter = 0
    for digit in password :
        if digit.isnumeric() :
            digit_counter += 1
    if digit_counter < 2 :
        return False


password = input()
is_pass_valid = [lenght_check(password), letter_and_digit_check(password), minimum_digit_check(password)]
if is_pass_valid[0] == is_pass_valid[1] == is_pass_valid[2] :
    print('Password is valid')
if is_pass_valid[0] == False :
    print('Password must be between 6 and 10 characters')
if is_pass_valid[1] == False :
    print('Password must consist only of letters and digits')
if is_pass_valid[2] == False :
    print('Password must have at least 2 digits')

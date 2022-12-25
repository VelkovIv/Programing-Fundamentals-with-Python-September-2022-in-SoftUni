___doc___ = """
Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines. 
A valid username:
•	has length between 3 and 16 characters inclusive
•	can contain only letters, numbers, hyphens, and underscores
•	has no redundant symbols before, after, or in between

---------------------------------------------------
Examples
---------------------------------------------------
--->Input
sh, too_long_username, !lleg@l ch@rs, jeffbutt
Output--->
jeffbutt
---------------------------------------------------
--->Input
Jeff, john45, ab, cd, peter-ivanov, @smith
Output--->
Jeff
John45
peter-ivanov

---------------------------------------------------
"""


def redundant_symbols(name):
    if ' ' in name:
        return False

    return True


def symbols_check_func(name):
    is_valid = True

    for character in name:
        if character.isalpha() or character.isnumeric() or character == '-' or character == '_':
            continue
        else:
            is_valid = False
            break
    return is_valid


def lenght_func(name):
    if 3 <= len(name) <= 16:
        return True

    return False


def is_username_valid(name):
    if lenght_func(name) and symbols_check_func(name) and redundant_symbols(name):
        return True

    return False


usernames = input().split(', ')

for username in usernames:
    if is_username_valid(username):
        print(username)

def palindrome_check(list) :
    check_list = []
    for number in range(len(list)) :
        if list[number] == list[number][::-1] :
            check_list.append('True')
        else:
            check_list.append('False')
    return check_list

list_of_numbers = input().split(', ')
print(*palindrome_check(list_of_numbers), sep='\n')

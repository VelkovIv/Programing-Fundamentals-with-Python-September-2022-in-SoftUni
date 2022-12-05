number = int(input())
string_number = str(number)
new_number = []
new_number[:0] = string_number
new_number.sort(reverse=True)
print(''.join(map(str,new_number)))

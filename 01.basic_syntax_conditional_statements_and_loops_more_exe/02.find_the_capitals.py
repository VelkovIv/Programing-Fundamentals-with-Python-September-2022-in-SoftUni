input_string = input()
upper_letter_indexes =[]
for index in range(len(input_string)):
    if input_string[index].isupper():
        upper_letter_indexes.append(index)

print(upper_letter_indexes)
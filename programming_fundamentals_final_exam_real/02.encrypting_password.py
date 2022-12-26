import re

number_of_inputs = int(input())

pattern = r'(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$'

for _ in range(number_of_inputs):
    current_input = input()
    data = re.findall(pattern, current_input)
    password = ''

    if len(data) >0:
        for index in range(len(data[0])):
            if index > 0:
                password += data[0][index]
        print(f'Password: {password}')
    else:
        print('Try another password!')
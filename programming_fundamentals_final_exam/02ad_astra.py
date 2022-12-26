import re

received_information = input()

total_calories = 0
result = ''

pattern = r'(\||#)([a-z A-Z]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'

data = re.findall(pattern, received_information) # extracting information from string by groups

for index in range(len(data)):
    item, date, calories = data[index][1], data[index][2], int(data[index][3])
    result += f'Item: {item}, Best before: {date}, Nutrition: {calories} \n' # preparing the print as f string
    total_calories += calories

days = int(total_calories/2000)
print(f'You have food to last you for: {days} days!')
print(result)

result = 'positive'
negative_counter = 0
zero_counter = 0
for i in range(1, 4) :
    current_number = int(input())
    if current_number < 0 :
        negative_counter += 1
    elif current_number == 0 :
        zero_counter += 1

if negative_counter > 0 and negative_counter % 2 != 0 :
    result = "negative"
if zero_counter > 0 :
    result = 'zero'

print(result)

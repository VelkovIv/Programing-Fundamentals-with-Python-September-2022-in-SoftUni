n = int(input())
kay_word = input()
full_list = []
filtered_list = []
for i in range(n) :
    current_string = input()
    full_list.append(current_string)
    if kay_word in current_string :
        filtered_list.append(current_string)
print(full_list)
print(filtered_list)

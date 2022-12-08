n = int(input())
full_list = []
filtered_list = []
for _ in range(n) :
    current_number = int(input())
    full_list.append(current_number)
command = input()

for i in range(len(full_list)) :
    if command == 'even' and full_list[i] % 2 == 0 or \
            command == 'odd' and full_list[i] % 2 != 0 or \
            command == 'positive' and full_list[i] >= 0 or \
            command == 'negative' and full_list[i] < 0 :
        filtered_list.append(full_list[i])
print(filtered_list)

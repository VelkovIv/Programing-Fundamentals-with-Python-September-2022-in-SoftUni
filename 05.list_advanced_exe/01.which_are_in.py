first_sequence = input().split(', ')
second_sequence = input().split(', ')
result = []
for index1 in range(len(first_sequence)) :
    for index2 in range(len(second_sequence)) :
        if first_sequence[index1] in second_sequence[index2] :
            result.append(first_sequence[index1])
            if result.count(first_sequence[index1])>1 :
                result.pop()
print(result)
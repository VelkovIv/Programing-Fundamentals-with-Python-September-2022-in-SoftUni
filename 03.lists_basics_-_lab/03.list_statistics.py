n = int(input())
positeve_list=[]
negative_list=[]
for i in range(n):
    current_number=int(input())
    if current_number>=0:
        positeve_list.append(current_number)
    else:
        negative_list.append(current_number)
print(positeve_list)
print(negative_list)
print(f'Count of positives: {len(positeve_list)}')
print(f'Sum of negatives: {sum(negative_list)}')
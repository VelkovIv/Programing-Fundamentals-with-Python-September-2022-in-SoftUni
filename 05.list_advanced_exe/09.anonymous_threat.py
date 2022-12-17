def megre(data, start_index, end_index) :
    if len(data) >= start_index :
        if start_index == 0 :
            return [''.join(data[start_index :end_index + 1])] + data[end_index + 1 :len(data)]
        elif start_index > 0 :
            return data[0 :start_index] + [''.join(data[start_index :end_index + 1])] + data[end_index + 1 :len(data)]
    else :
        return data


def devide(data, index, partition) :
    element_lenght = len(data[index])
    if len(data) > index :
        if index == 0:
            for character in data[index]:


                pass


        elif index > 0:
            pass
    else :
        return data


string = input().split(' ')
while True :
    command = input()
    if command == '3:1' :
        break
    action, start_index_or_index, end_index_or_partitions = command.split(' ')
    if action == 'merge' :
        string = megre(string, int(start_index_or_index), int(end_index_or_partitions))
    elif action == 'divide' :
        string = devide(string, int(start_index_or_index), int(end_index_or_partitions))
print(' '.join(string))

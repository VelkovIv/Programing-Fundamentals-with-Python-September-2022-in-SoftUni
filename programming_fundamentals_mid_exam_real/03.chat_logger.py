
def delete_func(chat_content, massage) :
    if massage in chat_content :
        chat_content.remove(massage)
    return chat_content


def edit_func(chat_content, old_version, new_version) :
    if old_version in chat_content :
        index_to_update = chat_content.index(old_version)
        chat_content.pop(index_to_update)
        chat_content.insert(index_to_update, new_version)
    return chat_content


def pin_func(chat_content, massage) :
    if massage in chat_content :
        current_index = chat_content.index(massage)
        chat_content.append(chat_content.pop(current_index))
    return chat_content


def spam_func(chat_content, current_command) :
    current_command.pop(0)
    for massage in range(len(current_command)) :
        chat_content.append(current_command[massage])

    return chat_content


chat_content = []

while True :

    command = input()
    if command == 'end' :
        break

    current_command = command.split(' ')

    if current_command[0] == 'Chat' :
        massage = current_command[1]
        chat_content.append(massage)
    elif current_command[0] == 'Delete' :
        chat_content = delete_func(chat_content, current_command[1])
    elif current_command[0] == 'Edit' :
        chat_content = edit_func(chat_content, current_command[1], current_command[2])
    elif current_command[0] == 'Pin' :
        chat_content = pin_func(chat_content, current_command[1])
    elif current_command[0] == 'Spam' :
        chat_content = spam_func(chat_content, current_command)

print('\n'.join(chat_content))

def add_func(messages, username, sent, received):
    # Creating a dictionary with key username and value list.
    # In the list at index 0 is number of sent messages and index 1 received messages.

    if username not in messages.keys():
        messages[username] = [sent, received]
        return messages


def message_func(messages, sender, receiver, capacity):
    if sender in messages and receiver in messages:
        messages[sender][0] += 1
        messages[receiver][1] += 1
        if messages[sender][0] + messages[sender][1] == capacity:
            del messages[sender]
            print(f'{sender} reached the capacity!')
        if messages[receiver][0] + messages[receiver][1] == capacity:
            del messages[receiver]
            print(f'{receiver} reached the capacity!')

        return messages


def empty_func(messages, username):

    if username in messages:
        del messages[username]

    if username == 'All':
        messages.clear()

    return messages


capacity_of_massage = int(input())
messages = {}
while True:
    current_command = input().split('=')

    if current_command[0] == 'Statistics':
        break

    if current_command[0] == 'Add':
        username, sent, received = current_command[1], int(current_command[2]), int(current_command[3])

        add_func(messages, username, sent, received)

    elif current_command[0] == 'Message':
        sender, receiver = current_command[1], current_command[2]

        message_func(messages, sender, receiver, capacity_of_massage)

    elif current_command[0] == 'Empty':
        username = current_command[1]

        empty_func(messages, username)

print(f'Users count: {len(messages)}')
for user, stat in messages.items():
    number_of_messages = stat[0] + stat[1]
    print(f'{user} - {number_of_messages}')

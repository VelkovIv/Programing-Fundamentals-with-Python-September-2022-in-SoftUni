def collect_func(journal, item) :
    if item not in journal :
        journal.append(item)

    return journal


def drop_func(journal, item) :
    if item in journal :
        journal.remove(item)

    return journal


def combile_items_func(journal, old_item, new_item) :
    if old_item in journal :
        index = journal.index(old_item)
        journal.insert(index + 1, new_item)

    return journal


def renew_func(journal, item) :
    if item in journal :
        journal.remove(item)
        journal.append(item)

    return journal


journal = input().split(', ')

while True :

    command = input()
    if command == 'Craft!' :
        break

    action, item = command.split(' - ')

    if action == 'Collect' :
        inventory = collect_func(journal, item)
    elif action == 'Drop' :
        inventory = drop_func(journal, item)
    elif action == 'Combine Items' :
        old_item, new_item = item.split(':')
        inventory = combile_items_func(journal, old_item, new_item)
    elif action == 'Renew' :
        inventory = renew_func(journal, item)

print(', '.join(inventory))

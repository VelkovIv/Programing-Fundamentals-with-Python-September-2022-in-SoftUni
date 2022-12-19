class Party :

    def __init__(self) :
        self.people = []

atendence = Party()
while True:
    command = input()

    if command == 'End':
        break

    name = command
    atendence.people.append(name)

print(f"Going: {', '.join(atendence.people)}")
print(f'Total: {len(atendence.people)}')
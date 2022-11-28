budget = int(input())
command=input()
no_more_money = False
while command !='End':
    price = int(command)
    budget -=price
    if budget <0:
        no_more_money = True
        break
    command = input()

if no_more_money:
    print('You went in overdraft!')
else:
    print('You bought everything needed.')
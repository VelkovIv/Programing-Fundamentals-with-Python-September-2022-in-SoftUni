def price_calculation(product, quantity) :
    if product == 'coffee' :
        print(f'{quantity * 1.5:.2f}')
    elif product == 'water' :
        print(f'{quantity * 1.0:.2f}')
    elif product == 'coke' :
        print(f'{quantity * 1.4:.2f}')
    elif product == 'snacks' :
        print(f'{quantity * 2.0:.2f}')


product = input()
quantity = int(input())

price_calculation(product, quantity)

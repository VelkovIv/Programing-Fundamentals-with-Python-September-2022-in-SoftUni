def drive_func(cars_, car_, distance_, fuel_):
    if cars_[car_][1] < fuel_:
        print('Not enough fuel to make that ride')
    elif cars_[car_][0] + distance_ >= 100000:
        print(f'{car_} driven for {distance_} kilometers. {fuel_} liters of fuel consumed.')
        print(f'Time to sell the {car}!')
        del cars_[car_]
    else:
        cars_[car_][0] += distance_
        cars_[car_][1] -= fuel_
        print(f'{car_} driven for {distance_} kilometers. {fuel_} liters of fuel consumed.')

    return cars_


def refuel_func(cars_, car_, fuel_):
    if cars_[car_][1] + fuel_ > 75:
        refuel = 75 - cars_[car_][1]
        cars_[car_][1] = 75
        print(f'{car_} refueled with {refuel} liters')
    else:
        cars_[car_][1] += fuel_
        print(f'{car_} refueled with {fuel_} liters')

    return cars_


def revert_func(cars_, car_, kilometers_):
    if cars_[car_][0] - kilometers_ < 10000:
        cars_[car_][0] = 10000
    else:
        cars_[car_][0] -= kilometers_
        print(f'{car_} mileage decreased by {kilometers_} kilometers')

    return cars_


number_of_cars = int(input())
cars = {}

for _ in range(number_of_cars):
    current_car = input().split('|')
    car, mileage, fuel = current_car[0], int(current_car[1]), int(current_car[2])
    # Create dictionary with car as key and list with two elements
    # on index 0 mileage and on index 1 fuel
    cars[car] = [mileage, fuel]

while True:
    current_command = input().split(' : ')

    if current_command[0] == 'Stop':
        break

    car = current_command[1]

    if current_command[0] == 'Drive':
        distance, fuel = int(current_command[2]), int(current_command[3])
        drive_func(cars, car, distance, fuel)
    elif current_command[0] == "Refuel":
        fuel = int(current_command[2])
        refuel_func(cars, car, fuel)
    elif current_command[0] == 'Revert':
        kilometers = int(current_command[2])

        revert_func(cars, car, kilometers)

for car, stat in cars.items():
    print(f'{car} -> Mileage: {stat[0]} kms, Fuel in the tank: {stat[1]} lt.')


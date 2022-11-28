number = int(input())

for i in range(number):
    currenr_number = int(input())
    if currenr_number % 2 != 0:
        print(f"{currenr_number} is odd!" )
        break
    if i == number-1:
        print("All numbers are even.")
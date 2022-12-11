incomes = input().split(", ")
number_of_beggans = int(input())
digit_incomes = []

beggan_incomes = []
for _ in range(len(incomes)) :
    digit_incomes.append(int(incomes[_]))
start_index = 0
for beggan in range(number_of_beggans) :
    beggan_income = 0
    for income in range(start_index, len(digit_incomes), number_of_beggans) :
        beggan_income += digit_incomes[income]
    beggan_incomes.append(beggan_income)
    start_index += 1
print(beggan_incomes)

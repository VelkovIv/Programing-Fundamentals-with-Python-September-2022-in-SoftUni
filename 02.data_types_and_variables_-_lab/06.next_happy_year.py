year = int(input())
# year-=1
is_happy_year = False
while is_happy_year != True :
    year+=1
    happy_year = set()
    for i in range(len(str(year))):
        happy_year.add(str(year)[i])
    is_happy_year = len(happy_year) == len(str(year))
print(year)


food_in_grams = float(input()) * 1000
hay_in_grams = float(input()) * 1000
cover_in_grams = float(input()) * 1000
guinea_pigs_weight_in_grams = float(input()) * 1000
is_something_finish = False
for day in range(1, 31) :
    food_in_grams -= 300
    if day % 2 == 0 :
        hay_in_grams -= food_in_grams * 0.05
    if day % 3 == 0 :
        cover_in_grams -= guinea_pigs_weight_in_grams / 3
    if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0 :
        is_something_finish = True
        break

if is_something_finish :
    print('Merry must go to the pet store!')
else :
    food_kg, hay_kg, cover_kg = food_in_grams / 1000, hay_in_grams / 1000, cover_in_grams / 1000
    print(
        f'Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.')

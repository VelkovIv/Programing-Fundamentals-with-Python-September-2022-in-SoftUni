number_of_snowballs = int(input())
best_snowball = 0
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0
for snowball in range(number_of_snowballs):
    current_snowball_weight = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())
    current_snowball = (current_snowball_weight / current_snowball_time) ** current_snowball_quality
    if current_snowball > best_snowball:
        best_snowball = int(current_snowball)
        best_snowball_weight = current_snowball_weight
        best_snowball_time = current_snowball_time
        best_snowball_quality = current_snowball_quality
print(f"{best_snowball_weight} : {best_snowball_time} = {best_snowball} ({best_snowball_quality})")
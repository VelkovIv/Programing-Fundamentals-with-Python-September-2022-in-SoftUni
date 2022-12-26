experience_to_unlock_tank = float(input())
count_of_battles = int(input())
gained_experience = 0
is_gain_experience = False
for battle in range(1, count_of_battles + 1) :
    current_battle_experience = float(input())
    gained_experience += current_battle_experience

    if battle % 3 == 0 :
        gained_experience += current_battle_experience * 0.15

    if battle % 5 == 0 :
        gained_experience -= current_battle_experience * 0.1

    if battle % 15 == 0 :
        gained_experience += current_battle_experience * 0.05

    if gained_experience >= experience_to_unlock_tank :
        is_gain_experience = True
        break

if is_gain_experience :
    print(f'Player successfully collected his needed experience for {battle} battles.')
else :
    needed_experience = experience_to_unlock_tank - gained_experience
    print(f'Player was not able to collect the needed experience, {needed_experience:.2f} more needed.')

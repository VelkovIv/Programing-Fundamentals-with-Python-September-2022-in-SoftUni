___doc___ = """
You are a pro MOBA player, you are struggling to become а master of the Challenger tier.
So, you carefully watch the statistics in the tier.
You will receive several input lines in one of the following formats:
"{player} -> {position} -> {skill}"
"{player} vs {player}"
The "player" and "position" are strings, and the given "skill" will be an integer number. 
You need to keep track of every player.
When you receive a player with his position and skill, add him to the players' pool, 
if he isn`t present, else add his position and skill or update his skill, 
only if the current position skill is lower than the new value.
If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
•	If they got at least one position in common, the player with better total skill points wins and the other 
    is demoted from the tier -> remove him. 
•	If they have same total skill points at the same positions, the duel is tie and they both continue in the Season.
•	If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
You should end your program when you receive the command "Season end". At that point you should print the players, 
ordered by total skill in descending order, then ordered by player name in ascending order. 
For each player print their position and skill, ordered descending by skill, then ordered by position name in ascending order.
Input / Constraints
•	The input comes in the form of commands in one of the formats specified above.
•	Player and position will always be one word string, containing no whitespaces.
•	Skill will be an integer in the range [0, 1000].
•	There will be no invalid input lines.
•	The program ends when you receive the command "Season end".
Output
•	The output format for each player is:
"{player}: {total_skills} skill"
- {position1} <::> {skill}
- {position2} <::> {skill}
…
- {positionN} <::> {skill}"

---------------------------------------------------
Examples
---------------------------------------------------
--->Input
Peter -> Adc -> 400
George -> Jungle -> 300
Simon -> Mid -> 200
Simon -> Support -> 250
Season end

Output--->
Simon: 450 skill
- Support <::> 250
- Mid <::> 200
Peter: 400 skill
- Adc <::> 400
George: 300 skill
- Jungle <::> 300

---------------------------------------------------
--->Input
Peter -> Adc -> 400
Bush -> Tank -> 150
Frank -> Mid -> 200
Frank -> Support -> 250
Frank -> Tank -> 250
Peter vs Frank
Frank vs Bush
Frank vs Hide
Season end

Output--->
Frank: 700 skill
- Support <::> 250
- Tank <::> 250
- Mid <::> 200
Peter: 400 skill
- Adc <::> 400

---------------------------------------------------
"""

moba_players_with_skills = {}

while True :
    command = input()

    if command == 'Season end' :
        break
    if ' -> ' in command :
        player, positions, skill = command.split(" -> ")
        skill = int(skill)

        if player in moba_players_with_skills.keys() and positions in moba_players_with_skills[player].keys() :
            if skill > moba_players_with_skills[player][positions] :
                moba_players_with_skills[player][positions] = skill
        else :
            if player not in moba_players_with_skills.keys() :
                moba_players_with_skills[player] = {positions : 0}
            moba_players_with_skills[player][positions] = skill

    elif 'vs' in command :
        player1, player2 = command.split(' vs ')

        if player1 in moba_players_with_skills.keys() and player2 in moba_players_with_skills.keys():
            total_skill_player1 = sum(moba_players_with_skills[player1].values())
            total_skill_player2 = sum(moba_players_with_skills[player2].values())

            player1_positions = []
            for skill, ponits in moba_players_with_skills[player1].items():
                 player1_positions.append(skill)

            for skill2, positions2 in moba_players_with_skills[player2].items():
                 if skill2 in player1_positions:
                    if total_skill_player1 > total_skill_player2:
                        del moba_players_with_skills[player2]
                        break
                    else:
                        del moba_players_with_skills[player1]

                        break

players_total_skils = {}
for player, positions in moba_players_with_skills.items() :
    for skill, points in positions.items() :
        if player not in players_total_skils.keys() :
            players_total_skils[player] = 0
        players_total_skils[player] += points

moba_players_with_skills_sorted = dict(sorted(moba_players_with_skills.items(), key= lambda x: sum(x[1].values()), reverse= True))

for player, skills in moba_players_with_skills_sorted.items() :
    print(f'{player}: {players_total_skils[player]} skill')
    for position, skill in sorted(skills.items(), key=lambda x : x[1], reverse=True) :
        print(f'- {position} <::> {skill}')

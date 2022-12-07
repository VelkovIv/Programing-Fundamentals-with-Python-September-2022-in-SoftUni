lost_fight_counts = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
arrmor_price = float(input())
helmet_brokes = lost_fight_counts // 2
sword_brokes = lost_fight_counts // 3
shield_brokes = lost_fight_counts // 6
arrmor_brokes = lost_fight_counts // 12
expenses = helmet_brokes * helmet_price + sword_brokes * sword_price + \
           shield_brokes * shield_price + arrmor_brokes * arrmor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")

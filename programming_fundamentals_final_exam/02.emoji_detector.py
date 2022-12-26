import re

pattern_emoji = r'(\*{2}|[:]{2})([A-Z][a-z]{2,})\1'
threshold = 1
coolness_emojis = []
sentence = input()

emojis = re.findall(pattern_emoji, sentence)
coolness = re.findall('\\d', sentence)

for number in coolness:
    threshold *= int(number)

for index in range(len(emojis)):
    coolness_sum = 0
    full_emoji = ''  # make emoji as in text with :: or ** in front or in back

    for symbol in emojis[index][1]:
        coolness_sum += ord(symbol)

    if coolness_sum >= threshold:
        full_emoji = emojis[index][0] + emojis[index][1] + emojis[index][0]
        coolness_emojis.append(full_emoji)

print(f'Cool threshold: {threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
print('\n'.join(coolness_emojis))

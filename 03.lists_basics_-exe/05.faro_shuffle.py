deck_of_cards = input().split()
number_of_shuffles = int(input())
middle_of_deck = len(deck_of_cards) // 2
for suffles in range(number_of_shuffles) :
    final_deck = []
    left_deck = deck_of_cards[:middle_of_deck]
    right_deck = deck_of_cards[middle_of_deck :]
    for deck_index in range(middle_of_deck) :
        final_deck.append(left_deck[deck_index])
        final_deck.append(right_deck[deck_index])
    deck_of_cards = final_deck
print(final_deck)
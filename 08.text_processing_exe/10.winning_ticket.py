___doc___ = """
The lottery is exciting. However, checking a million tickets for winnings only by hand is not. 
So, you are given the task of creating a program that automatically checks if a ticket is a winner.
You are given a collection of tickets separated by commas and spaces (one or many). 
You need to check each ticket to see if it has a winning combination of symbols:
•	A valid ticket has exactly 20 characters.
•	A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly repeated 
at least 6 times in both halves of the tickets.
•	In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
An example of a valid winning ticket:
"Cash$$$$$$Ca$$$$$$sh"
An example of a Jackpot winning valid ticket:
"$$$$$$$$$$$$$$$$$$$$"
Input
The input will be read from the console. The input consists of a single line containing all tickets 
separated by commas and one or more white spaces in the format:
•	"{ticket}, {ticket}, … {ticket}"
Output
Print the result for every ticket in the order of their appearance, each on a separate line in the format:
•	If the ticket is invalid: "invalid ticket"
•	If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
•	If the ticket is valid and winning, but not a Jackpot: 
"ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
•	It the ticket hits the Jackpot:
"ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"
Constrains
•	Number of tickets will be in range [0 … 100]


---------------------------------------------------
Examples
---------------------------------------------------
--->Input
Cash$$$$$$Ca$$$$$$sh
Output--->
ticket "Cash$$$$$$Ca$$$$$$sh" - 6$
---------------------------------------------------
--->Input
$$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey
Output--->
ticket "$$$$$$$$$$$$$$$$$$$$" - 10$ Jackpot!
invalid ticket
ticket "th@@@@@@eemo@@@@@@ey" - 6@

---------------------------------------------------
--->Input
validticketnomatch:(, Cas$$$$$$$Ca$$$$$$s$
Output--->
ticket "validticketnomatch:(" - no match
ticket "Cas$$$$$$$Ca$$$$$$s$" - 6$

---------------------------------------------------
"""


def ticket_validation(ticket):
    winning_symbols = ['@', '#', '$', '^']
    if len(ticket) == 20:
        left_part = ticket[:10]
        right_part = ticket[10:]
        for symbol in winning_symbols:

            for number_of_symbols in range(10, 5, -1):
                group_of_symbols = number_of_symbols * symbol

                if group_of_symbols in left_part and group_of_symbols in right_part:

                    if number_of_symbols == 10:
                        return f'ticket "{ticket}" - {number_of_symbols}{symbol} Jackpot!'

                    else:
                        return f'ticket "{ticket}" - {number_of_symbols}{symbol}'

        return f'ticket "{ticket}" - no match'

    return "invalid ticket"


tickets = [element.strip() for element in input().split(', ')]

for ticket in tickets:
    print(ticket_validation(ticket))

import random
from cards import cards
from art import logo
def Blackjack():
    """Blackjack(None) Game."""
    print(logo)
    user_cards = []
    comp_cards = []
    for _ in range(2):
        comp_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
    user_score = sum(user_cards)
    comp_score = sum(comp_cards)
    while comp_score < 17:
        comp_cards.append(random.choice(cards))
        if 11 in comp_cards and sum(comp_cards) > 21:
            comp_cards.remove(11)
            comp_cards.append(1)
        comp_score += comp_cards[-1]

    passed = False
    while not passed:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card is: {comp_cards[0]}")
        n_card = ""
        new_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if new_card == 'y':

            user_cards.append(random.choice(cards))
            if 11 in user_cards and sum(user_cards) > 21:
                user_cards.remove(11)
                user_cards.append(1)
            user_score += user_cards[-1]

            if user_score > 21:
                passed = True
        else:
            passed = True

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card is: {comp_cards}")
    if user_score > 21:
        print("You went over 21, You lose :(. ")
    elif comp_score > 21:
        print("Computer went over 21,  You win!. ")
    elif user_score > comp_score:
        print("You Won! ")
    else:
        print("You lose! ")
    new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if new_game == 'y':
        Blackjack()
    else:
        return 0


Game = input("Do want to play BlackJack? Type 'y' or 'n': ")
if Game == 'y':
    Blackjack()
else:
    print("Have a good day. ")
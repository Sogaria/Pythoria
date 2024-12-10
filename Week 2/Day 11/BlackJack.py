import random

def ListSum(liste: list) -> int:
    return sum(liste)

def DrawCard():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(deck)
    return deck[0]

def ComputerDeckFill(npc_deck: list):
    while ListSum(npc_deck) <= 15:
        npc_deck.append(DrawCard())
    ReplaceAce([], npc_deck)  # Replace Aces in the NPC's deck if necessary

def CalcWin(player_deck: list, npc_deck: list):
    print(f"   Your final hand: {player_deck}, final score: {ListSum(player_deck)}")
    print(f"   Computer's final hand: {npc_deck}, final score: {ListSum(npc_deck)}")
    if ListSum(npc_deck) == 21:
        print("You lose! Computer has blackjack!")
    elif ListSum(player_deck) > 21:
        print("You busted! Computer wins!")
    elif ListSum(npc_deck) > 21 or ListSum(player_deck) > ListSum(npc_deck):
        print("You won! Congratulations!")
    else:
        print("You lost to the computer!")

def ReplaceAce(player_deck: list, npc_deck: list):
    # Replace Aces in player's deck
    while 11 in player_deck and ListSum(player_deck) > 21:
        player_deck.remove(11)
        player_deck.append(1)
    
    # Replace Aces in computer's deck
    while 11 in npc_deck and ListSum(npc_deck) > 21:
        npc_deck.remove(11)
        npc_deck.append(1)

while True:
    player_deck = []
    npc_deck = []
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "n":
        break
    else:
        player_deck.append(DrawCard())
        player_deck.append(DrawCard())
        npc_deck.append(DrawCard())
        print(f"Your cards: {player_deck}, current score: {ListSum(player_deck)}")
        print(f"Computer's first card: {npc_deck[0]}")
        draw_next = "y"
        while ListSum(player_deck) < 21:
            draw_next = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_next == "n":
                break
            player_deck.append(DrawCard())
            ReplaceAce(player_deck, [])
            print(f"Your cards: {player_deck}, current score: {ListSum(player_deck)}")
            print(f"Computer's first card: {npc_deck[0]}")
        
        # Fill the computer's deck
        ComputerDeckFill(npc_deck)

        # Handle cases where the computer's deck exceeds 21
        while ListSum(npc_deck) > 21:
            ReplaceAce([], npc_deck)
            if 11 not in npc_deck:  # Exit if no more Aces to replace
                break

        CalcWin(player_deck, npc_deck)





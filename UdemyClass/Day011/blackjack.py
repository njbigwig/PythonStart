# DO NOT RUN UNDER GIT BASH WINDOW

# Blackjack rules
# 2 - 10 = number
# Face cards = 10
# Ace = 1 or 11
# tie = draw
# If dealer < 17, must take another card

import random

# random.shuffle(deck_of_cards)

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#card_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
card_names = ["2 Card", "3 Card", "4 Card", "5 Card", "6 Card", "7 Card", "8 Card", "9 Card", "10 Card", "Jack", "Queen", "King", "Ace"]
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
card_suits  = ["\u2663", "\u2665", "\u2666", "\u2660"] 

deck_of_cards =[]

def create_deck_of_cards(numdecks):
    
    for decks in range(numdecks):
        for suits in card_suits:
            for names in card_names:
                deck_of_cards.append([suits, names, card_values[card_names.index(names)]])
       
    random.shuffle(deck_of_cards)
    
    # TEST: print out deck to verify completeness and shuffling
    # print(len(deck_of_cards))
    # for cards in deck_of_cards:
    #     print(f"{cards[0]} {cards[1]} {cards[2]}")
    return(len(deck_of_cards))

def show_player_hand(player_hand):
    card_count = 0
    ace_flag = False
    
    print("\nPlayer's Hand:")
    
    for card in player_hand:
        print(f"{card[0]}-{card[1]}")
        
        if card[1] == "Ace":
            ace_flag = True
            
        card_count += card[2]
        
    
    
    # adjust for Ace
    if len(player_hand) > 2 and card_count > 21 and ace_flag == True:
        #print("Player Ace adj")
        card_count -= 10
        
    print(f"Showing: {card_count}\n")
        
    return card_count

def show_dealer_hand(dealer_hand):
    card_count = 0
    ace_flag = False
    showed_first_card = False
    
    print("\nDealer's Hand:")
    
    for card in dealer_hand:
        if showed_first_card == False:
            print(f"{card[0]}-{card[1]}")
            showed_first_card = True
        else:
            print("XX-XX")
            
        if card[1] == "Ace":
            ace_flag = True
            
        card_count += card[2]
    
    # adjust for Ace
    if len(dealer_hand) > 2 and card_count > 21 and ace_flag == True:
        #print("Dealer Ace adj")
        card_count -= 10    
        
    print(f"Showing: {dealer_hand[0][2]}\n")
    
    return card_count

def winner_check(player, dealer):
    if player == 21:
       return True
    elif dealer == 21:
        return True
    elif player > 21:
        return True
    elif dealer > 21:
        return True
    else:
        return False
        
# start of main program    
user_cmd = "y"

winner = False
total_cards = 0

while user_cmd == "y":
    user_cmd = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    number_decks = 0
    
    if user_cmd == "y":
        # play 21
        print(f"{logo}\n")
        while number_decks == 0:
            number_decks = int(input("How many decks, type 1-10: "))
            if number_decks > 10:
                print("Too many decks, try again...\n")
                number_decks = 0
    
        # create a shuffled deck
        deck_of_cards = []
        total_cards = create_deck_of_cards(number_decks)
        
        player_hand = []
        player_hand_count = 0
        
        dealer_hand = []
        dealer_hand_count = 0
        
        # alternate dealing first 4 cards to player then dealer, taking from the top
        get_a_card = deck_of_cards.pop(0)
        player_hand.append([get_a_card[0], get_a_card[1], get_a_card[2]])
        
        get_a_card = deck_of_cards.pop(0)
        dealer_hand.append([get_a_card[0], get_a_card[1], get_a_card[2]])
        
        get_a_card = deck_of_cards.pop(0)
        player_hand.append([get_a_card[0], get_a_card[1], get_a_card[2]])
        
        get_a_card = deck_of_cards.pop(0)
        dealer_hand.append([get_a_card[0], get_a_card[1], get_a_card[2]]) 
        
        total_cards = len(deck_of_cards)
                      
        player_hand_count = show_player_hand(player_hand)
        
        dealer_hand_count = show_dealer_hand(dealer_hand)
        
        #print(f"Player {player_hand_count}")     
        #print(f"Dealer {dealer_hand_count}")  
        
        winner = winner_check(player_hand_count, dealer_hand_count)
       
        while winner == False and total_cards > 0:
            print(f"Cards remaining: {total_cards}")  
            dealer_cmd = input("Type 'y' to get another card, type 'p' to pass, type 'c' to call: ").lower()
            
            if dealer_cmd == "y":
                # player wants another card
                get_a_card = deck_of_cards.pop(0)
                player_hand.append([get_a_card[0], get_a_card[1], get_a_card[2]])
                player_hand_count = show_player_hand(player_hand)
                total_cards = len(deck_of_cards)
            elif dealer_cmd == "p" and dealer_hand_count < 17:
                get_a_card = deck_of_cards.pop(0)
                dealer_hand.append([get_a_card[0], get_a_card[1], get_a_card[2]])
                dealer_hand_count = show_dealer_hand(dealer_hand)
                total_cards = len(deck_of_cards)
            elif dealer_cmd == "c":
                total_cards = 0
                
            winner = winner_check(player_hand_count, dealer_hand_count)
        
        print(f"Dealer has: {dealer_hand_count} Player has: {player_hand_count}")    
        
        if player_hand_count == dealer_hand_count:
            print("It is a DRAW!")
        elif player_hand_count > 21:
            print("You LOSE!")
        elif dealer_hand_count > 21:
            print("You WIN!!!!")
        elif player_hand_count == 21:
            print("You WIN!!!!")
        elif dealer_hand_count == 21:
            print("House WINS!")
        elif dealer_hand_count > player_hand_count:
            print("House WINS!")
        elif player_hand_count > dealer_hand_count:
            print("You WIN!!!!")
            
                
                


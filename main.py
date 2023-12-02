import random
import os

# Set up the deck
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
          'Ace': 11}
money: int
bet: int

deck = []
for suit in suits:
    for rank in ranks:
        deck.append((rank, suit))

random.shuffle(deck)

# Deal player and dealer hands
player_hand = []
dealer_hand = []
for i in range(1):
    dealer_hand.append(deck.pop())
for i in range(2):
    player_hand.append(deck.pop())

money = int(input("How much money would you like to deposit? $"))
bet = int(input("How much would you like to bet? $"))

# Players turn
while True:
    print("\nDealer Showing:", *dealer_hand, "('?', '???')", sep='\n')
    print("\nPlayer Hand:", *player_hand, sep='\n')
    print("Player Hand Total:", sum(values[rank] for rank, suit in player_hand))

    hit_or_stand = input("Hit or Stand? (h/s) ")
    if hit_or_stand == 'h':
        os.system('clear')
        player_hand.append(deck.pop())
        if sum(values[rank] for rank, suit in player_hand) > 21:
            print("Player Hand:", *player_hand, sep='\n')
            print("Player Hand Total:", sum(values[rank] for rank, suit in player_hand))
            print("\nBust! Dealer wins.\nMoney Available: $", money - bet)
            break
    elif hit_or_stand == 's':
        break

# Dealers turn
if sum(values[rank] for rank, suit in player_hand) <= 21:

    while sum(values[rank] for rank, suit in dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print("\nDealer Hand:", *dealer_hand, sep='\n')
    print("Dealer Hand Total:", sum(values[rank] for rank, suit in dealer_hand))

    if sum(values[rank] for rank, suit in dealer_hand) > 21:
        print("Dealer Busts! You win.\nMoney Available: $", money + bet)
    elif sum(values[rank] for rank, suit in dealer_hand) < sum(values[rank] for rank, suit in player_hand):
        print("You win!\nMoney Available: $", money + bet)
    elif sum(values[rank] for rank, suit in dealer_hand) > sum(values[rank] for rank, suit in player_hand):
        print("Dealer wins.\nMoney Available: $", money - bet)
    else:
        print("It's a tie.\nMoney Available: $", money)

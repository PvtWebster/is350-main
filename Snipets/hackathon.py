'''
A simple game of blackjack - coded for course IST 350 at UWM during Fall 2022
Authors: Richard Mogilka, Nicholas Lofy, and Gavin Henry
'''
#card class
class Card:
	def __init__(self, rank, suit):
			self.rank = rank
			self.suit = suit

#hand class, aka player or dealer
class Hand:
	def __init__(self, name, cards, value, size):
		self.name = name
		self.cards = cards
		self.value = value
		self.size = size

#initialize deck
def build_deck():
	rank = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
	for value in rank:
		for suit in suits:
			new_card = Card(value, suit)
			deck.append(new_card)
			#print(f"{new_card.rank} of {new_card.suit}")
	return deck

#deal initial hand
def deal_hand(player):
	while (player.size < 2):
		deal_card(player)

#get card's int value
def card_value(card, hand_value):
	card_value = card.rank
	if (card.rank == "A"):
		if (hand_value <= 10):
			card_value = 11
		else:
			card_value = 1
	elif ((card.rank == "J") or (card.rank == "Q") or (card.rank == "K")):
		card_value = 10

	return card_value

#deal a single card if card is in deck, otherwise do nothing
def deal_card(player):
	index = random.randint(0,51) #NOTE: RANDOM IS NOT EXCLUSIVE FOR END - (0,52) will create 'OutOfBounds' Exception
	#print(f"index =  {index}")
	card = deck[index]
	if (valDeck[index] == 1):
		player.cards.append(card)
		valDeck[index] = 0;
		player.value = player.value + card_value(card, player.value)
		player.size += 1

#print player hand
def show_hand(player):
	print(f"{player.name.title()} has: ", end="")
	for card in player.cards:
		print(f"{card.rank} of {card.suit}", end=", ")
	print(f"Total Hand Value = {player.value}")

#special print for dealer hand when one card hidden
def show_dealer(dealer):
	print(f"Dealer showing: {dealer.cards[0].rank} of {dealer.cards[0].suit}")

#############################MAIN###########################################
import random
#variables
player_input = "yes"
chips = 100
deck = []
build_deck()
player = Hand("player", [], 0, 0)
dealer = Hand("dealer", [], 0, 0)
#############################GAME###########################################
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
print("~*~*~*~*~*~*~*~*~*~*WELCOME TO BLACKJACK~*~*~*~*~*~*~*~*~*~*")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
#outer while loop: checks if player has chips to play, or choses to quit game
while ((chips > 0) and (player_input == "yes")):
	bet = int(input("Place your bet : "))#take bet before cards are dealt
	while (bet > chips):#bet validation loop
		print(f"Error: Bet amount '{bet}' exceeds chips total '{chips}'. Please bet again.")
		bet = int(input("Place your bet : "))
	#initialize validation deck
	valDeck = []
	for card in range(0,52):
		valDeck.append(1)
	#deal initial hands to player and dealer
	deal_hand(player)
	deal_hand(dealer)
	show_hand(player)
	show_dealer(dealer)
	
	#player's inner while loop - exit condition(s): player doesn't hit, player busts
	while(player.value < 21):
		print()
		choice=input("Would you like to hit or stand? (hit/stand) ").lower() #player.value
		print("")
	
		if(choice=='hit'):
			deal_card(player)
			show_hand(player)
			
		elif(choice == 'stand'):
			show_hand(player)
			break
	
	#dealers inner while loop - exit condition(s): dealer busts, dealer doesn't hit (dealer stands on 17(?))
	while (dealer.value < 17):
		deal_card(dealer)
	#show dealer's final hand
	if(dealer.value >=17):
		show_hand(dealer)

	#choose winner - based on rules of blackjack, there is an order to follow: do if 'then' else if to ensure that only ONE decision returns
	if (player.value > 21):#first check if player busted
		chips = chips - bet
		print(f"{player.name} busted! You lose! You now have {chips} remaining.")
	elif(dealer.value > 21):#check if dealer busted
		chips = chips + bet
		print(f"Dealer busted! You win! You now have {chips} remaining.")
	elif(player.value == dealer.value):#check if player and dealer have same total
		print("Push! Take back your chips!\n")
	else:#no busts and no tie, so one hand beats the other
		if(player.value > dealer.value):#player wins
			chips = chips + bet
			print(f"You win! You now have {chips} remaining.")
		else:#dealer wins
			chips = chips - bet
			print(f"You lose! You now have {chips} remaining.")
	
#outer while loop exit check, user prompt for else
	if (chips <= 0):
		print("GAME OVER!")
	else:
		#reset class values for player and dealer
		player.cards = []; player.value = 0; player.size = 0; dealer.cards = []; dealer.value = 0; dealer.size = 0;
		player_input = input("Would you like to play again? (yes/no) ").lower()
		if (player_input == "no"):
			print(f"You finished with {chips} chips!")
			print("Thanks for playing!")
#end outer while loop
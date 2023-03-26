#The evaluate hands function works and is fully functional giving the correct result
#However, the determine winner function has errors which will be rectified in future
#Not currently being modified


rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
hand_ranks = {'High card': 1, 'Pair': 2, 'Two pair':3, "Three of a kind" : 4, "Straight": 5, "Flush": 6, "Full house":7, "Four of a kind":8, "Straight flush":9, "Royal Flush":10}
import random
from itertools import combinations

class Player:
	def __init__(self, name):
		self.name = name
		self.hands = []
		self.hand = []
		self.evaluator = Hand_evaluator()

	def __repr__(self):
		return self.name

	def take_card(self, card):
		self.hand.append(card)

	def __gt__(self,other):
		return self.evaluator.__gt__(other.evaluator)
 

class Deck:
	def __init__(self):
		self.deck = []
		suits = ["H", "D", "S", "C"]
		ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
		for suit in suits:
			for rank in ranks:
				self.deck.append(rank + suit)

	def shuffle_deck(self):
		random.shuffle(self.deck)


	def deal_card(self):
		card = self.deck[0]
		self.deck = self.deck[1:]
		return card
	
class Table:
	def __init__(self):
		self.community_cards = []
		self.players = []

	def add_player(self,player):
		self.players.append(player)

	def form_hands(self, player):
		combs_calc = list(combinations((self.community_cards + player.hand),5))
		hands = [hand for hand in combs_calc]
		player.hands = []
		for hand in hands:
			my_dict = {"ranks": {}, "suits": {}}  
			ranks = {}
			suits = {}
			for card in hand:
				rank = card[0]
				if rank in ranks:
					ranks[rank] += 1
				else:
					ranks[rank] = 1
				suit = card[1]
				if suit in suits:
					suits[suit] += 1
				else:
					suits[suit] = 1
	        #The ranks are sorted 
			sorted_ranks = sorted(ranks, key=lambda x: (ranks[x] == 1, rank_values[x])) 
			my_dict["ranks"] = {rank: ranks[rank] for rank in sorted_ranks}
	        # suit total is calculated
			my_dict["suits"] = len(suits)
			#each dict added (each hand added)
			player.hands.append(my_dict)
		return player.hands

	def evaluate_hand(self, hand_dict):
			l = list(hand_dict["ranks"].items())
			if hand_dict['suits'] == 1:
				if 'T' in hand_dict['ranks'] and 'J' in hand_dict['ranks'] and 'Q' in hand_dict['ranks'] and 'K' in hand_dict['ranks'] and 'A' in hand_dict['ranks']:
					return 'Royal flush' #we already know suits == 1, jump to flush instead of four of a kind and full house
				if (rank_values[l[4][0]]-rank_values[l[0][0]] == 4) or (l[4][0] == "A" and l[3][0] == "5"):
					return "Straight flush" 
				return "Flush"
			if l[0][1] == 4:  #most common rank occurs 4 times
				return "Four of a kind" 
			#full house: length ranks = 2, first value = 3
			if len(l) == 2:
				return "Full house"
			if len(l) == 5:
				if (rank_values[l[4][0]]-rank_values[l[0][0]] == 4) or (l[4][0] == "A" and l[3][0] == "5"):
					return "Straight"
				return "High card"
			if len(l) == 3:
				if l[0][1] == 3:
					return "Three of a kind"
				return "Two pair"
			if l[0][1] == 2:
				return "Pair"

	def evaluate_hands(self):
		for player in self.players:
			for hand in player.hands:
				hand_type = self.evaluate_hand(hand)
				player.evaluator.all_ranks.append(hand_type)
				if hand_type == "Royal Flush":
					player.evaluator.royal_flushes.append(Hand_evaluator.custom_sort(hand))
				elif hand_type == "Straight Flush":
					player.evaluator.straight_flushes.append(Hand_evaluator.custom_sort(hand))
				elif hand_type == "Four of a kind":
					player.evaluator.four_of_a_kinds.append(Hand_evaluator.custom_sort(hand))
				elif hand_type == "Full house":
					player.evaluator.full_houses.append(Hand_evaluator.custom_sort(hand))
				elif hand_type == "Flush":
					player.evaluator.flushes.append(Hand_evaluator.custom_sort(hand))
				elif hand_type == "Straight":
					player.evaluator.straights.append(Hand_evaluator.custom_sort(hand))
				elif hand_type == "Three of a kind":
					player.evaluator.three_of_a_kinds.append(Hand_evaluator.custom_sort(hand))
				elif hand_type == "Two pair":
					player.evaluator.two_pairs.append(Hand_evaluator.custom_sort(hand))
				elif hand_type == "Pair":
					player.evaluator.pairs.append(Hand_evaluator.custom_sort(hand))
				elif hand_type == "High card":
					player.evaluator.high_cards.append(Hand_evaluator.custom_sort(hand))
			player.evaluator.all_ranks = sorted(player.evaluator.all_ranks, key = hand_ranks.get, reverse = True)

	def determine_winner(self):
		max_rank = max(player.evaluator.all_ranks[0] for player in self.players)
		self.winner = [player for player in self.players if player.evaluator.all_ranks[0] == max_rank]
		if len(self.winner) == 1:
			return f"{self.winner[0]} is the winner!\nHand rank: {self.winner[0].evaluator.all_ranks[0]}\nHand:{self.winner[0].evaluator.best_hand()}"
		else:
			for i in range(len(self.winner[0].evaluator.best_hand())):
				highest_cards = [player.evaluator.best_hand()[i] for player in self.winner]
				max_card = max(highest_cards)
				new_winners = self.winner
				for player in new_winners:
					if player.evaluator.best_hand()[i] < max_card:
						self.winner.remove(player)
				if len(self.winner) == 1:
					break
			if len(self.winner) == 1:
				return f"{self.winner[0]} is the winner!\nHand rank: {self.winner[0].evaluator.all_ranks[0]}\nHand:{self.winner[0].evaluator.best_hand()}"
			else:
				return f"Draw between:{self.winner}\n Hand rank: {self.winner[0].evaluator.all_ranks[0]}\nHand:{self.winner[0].evaluator.best_hand()}"
	
class Hand_evaluator:
	def __init__(self):
		self.all_ranks = []
		self.royal_flushes = []
		self.straight_flushes = []
		self.four_of_a_kinds = []
		self.full_houses = []
		self.flushes = []
		self.straights = []
		self.three_of_a_kinds = []
		self.two_pairs = []
		self.pairs = []
		self.high_cards = []

	def custom_sort(hand):
		return dict(sorted(hand["ranks"].items(), key=lambda x: (-x[1],-rank_values[x[0]])))

	def best_hand(self):
		if self.royal_flushes:
			return self.royal_flushes[0]
		if self.straight_flushes:
			return self.best_straight_flush(self.straight_flushes)
		if self.four_of_a_kinds:
			return self.best_four_of_a_kind(self.four_of_a_kinds)
		if self.full_houses:
			return self.best_full_house(self.full_houses)
		if self.straights:
			return self.best_straight(self.straights)
		if self.flushes:
			return self.best_flush(self.flushes)
		if self.three_of_a_kinds:
			return self.best_three_of_a_kind(self.three_of_a_kinds)
		if self.two_pairs:
			return self.best_two_pair(self.two_pairs)
		if self.pairs:
			return self.best_pair(self.pairs)
		if self.high_cards:
			return self.best_high_card(self.high_cards)


	def best_flush(self,flushes):
		if not self.flushes:
			return None
		flush_list = [[rank_values[key] for key, value in hand.items()] for hand in self.flushes]
		my_list = flush_list.copy()
		for i in range(5):
			maximum = max(l[i] for l in my_list)
			for l in my_list:
				if l[i] < maximum:
					my_list.remove(l)
		return my_list[0]


	def best_straight_flush(self,flushes):
		if not self.straight_flushes:
			return None
		straight_flush_list = [[rank_values[key] for key, value in hand.items()] for hand in self.straight_flushes]
		my_list = straight_flush_list.copy()
		for l in my_list:
			if 14 in l and 2 in l:
				l[0] = 1
				ace = l.pop(0)
				l.insert(4,ace)
		for i in range(5):
			maximum = max(l[i] for l in my_list)
			for l in my_list:
				if l[i] < maximum:
					my_list.remove(l)
		return my_list[0]


	def best_four_of_a_kind(self,four_of_a_kinds):
		if not self.four_of_a_kind:
			return None
		four_list = [[rank_values[key] for key, value in hand.items()] for hand in self.four_of_a_kinds]
		my_list = four_list.copy()
		for i in range(2):
			maximum = max(l[i] for l in my_list)
			for l in my_list:
				if l[i] < maximum:
					my_list.remove(l)
		return my_list[0]

	def best_full_house(self,full_houses):
		if not self.full_houses:
			return None
		four_list = [[rank_values[key] for key, value in hand.items()] for hand in self.full_houses]
		my_list = four_list.copy()
		for i in range(2):
			maximum = max(l[i] for l in my_list)
			for l in my_list:
				if l[i] < maximum:
					my_list.remove(l)
		return my_list[0]


	def best_straight(self,straights):
		if not self.straights:
			return None
		straights_list = [[rank_values[key] for key, value in hand.items()] for hand in self.straights]
		my_list = straights_list.copy()
		for l in my_list:
			if 14 in l and 2 in l:
				l[0] = 1
				ace = l.pop(0)
				l.insert(4,ace)
		for i in range(5):
			maximum = max(l[i] for l in my_list)
			for l in my_list:
				if l[i] < maximum:
					my_list.remove(l)
		return my_list[0]

	def best_three_of_a_kind(self,three_of_a_kinds):
		if not self.three_of_a_kinds:
			return None
		threes_list = [[rank_values[key] for key, value in hand.items()] for hand in self.three_of_a_kinds]
		my_list = threes_list.copy()
		for i in range(3):
				maximum = max(l[i] for l in my_list)
				for l in my_list:
					if l[i] < maximum:
						my_list.remove(l)
		return my_list[0]

	def best_two_pair(self,two_pairs):
		if not self.two_pairs:
			return None
		twos_list = [[rank_values[key] for key, value in hand.items()] for hand in self.two_pairs]
		my_list = twos_list.copy()
		for i in range (3):
			maximum = max(l[i] for l in my_list)
			for l in my_list:
				if l[i] < maximum:
					my_list.remove(l)
		return my_list[0]

	def best_pair(self,pairs):
		if not self.pairs:
			return None
		pairs_list = [[rank_values[key] for key, value in hand.items()] for hand in self.pairs]
		my_list = pairs_list.copy()
		for i in range(4):
			maximum = max(l[i] for l in my_list)
			for l in my_list:
				if l[i] < maximum:
					my_list.remove(l)
		return my_list[0]

	def best_high_card(self,high_cards):
		if not self.high_cards:
			return None
		high_list = [[rank_values[key] for key, value in hand.items()] for hand in self.high_cards]
		my_list = high_list.copy()
		for i in range(5):
			maximum = max(l[i] for l in my_list)
			for l in my_list:
				if l[i] < maximum:
					my_list.remove(l)
		return my_list[0]

	def __gt__(self,other):
		type_order = ["High card", "Pair", "Two pair", "Three of a kind", "Straight", "Flush", "Full house", "Four of a kind", "Straight flush", "Royal flush"]
		if type_order.index(self.all_ranks[0]) > type_order.index(other.all_ranks[0]):
			return True
		else:
			return False

	def __eq__(self,other):
		type_order = ["High card", "Pair", "Two pair", "Three of a kind", "Straight", "Flush", "Full house", "Four of a kind", "Straight flush", "Royal flush"]
		if type_order.index(self.all_ranks[0]) == type_order.index(other.all_ranks[0]):
			return True
		else:
			return False



Millie = Player("Millie")
James = Player("James")
Bob = Player("Bob")
Jack = Player("Jack")

my_deck = Deck()
my_deck.shuffle_deck()

my_table = Table()

my_table.add_player(Millie)
my_table.add_player(James)
my_table.add_player(Bob)
my_table.add_player(Jack)

for i in range(2):
	for player in my_table.players:
		next_card = my_deck.deal_card()
		player.take_card(next_card)
for i in range(5):
	next_card = my_deck.deal_card()
	my_table.community_cards.append(next_card)


millie_hands = my_table.form_hands(Millie)
james_hands = my_table.form_hands(James)
bob_hands = my_table.form_hands(Bob)
jack_hands = my_table.form_hands(Jack)

my_table.evaluate_hands()



print(my_table.determine_winner())

				
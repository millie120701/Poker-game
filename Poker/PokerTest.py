from PlayingCards import Player, Deck, Table, Hand_evaluator
rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
hand_ranks = {'High card': 1, 'Pair': 2, 'Two pair':3, "Three of a kind" : 4, "Straight": 5, "Flush": 6, "Full house":7, "Four of a kind":8, "Straight flush":9, "Royal Flush":10}


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

#does all evaluations on each dict from player.hands, results accessed by player.evaluator (note self.evaluator = Hand_evaluator())
#__gt__ also used in the player class (defined in the Hand_evaluator class, so Millie > James would return True/False, __eq__ also in 
my_table.evaluate_hands()

print(my_table.determine_winner()) #returns winner, not the runner ups. If there is a tie, their hand is returned and the rank. 

#player.evaluator.flushes would return flushes
#player.evaluator.best_hand() returns best hand
#player.evaluator.all_ranks would show all the ranks the person possesses in descending order
#player.hands returns all hands the player has (in dict form)
#player.hand returns player's two cards
print(Millie.evaluator.best_hand())
print(James.evaluator.best_hand())
print(Jack.evaluator.best_hand())
print(Bob.evaluator.best_hand())



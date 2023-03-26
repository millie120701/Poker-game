
rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

hand_ranks = {'Card high': 1, 'Pair': 2, 'Two pair':3, "Three of a kind" : 4, "Straight": 5, "Flush": 6, "Full house":7, "Four of a kind":8, "Straight flush":9, "Royal Flush":10}





"""
class Player:
    def __init__(self, name):
        self.name = name
        self.combinations = {}
        self.hand = []

    def __repr__(self):
        return self.name
    
    def take_card(self, card):
        self.hand.append(card)


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
        hands = (list(comb) for comb in combs_calc)
        all_dicts = []
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
            # Sort the rank counts
            sorted_ranks = sorted(ranks, key=lambda x: (ranks[x] == 1, rank_values[x]))
            my_dict["ranks"] = {rank: ranks[rank] for rank in sorted_ranks}
            # Get the total number of suits
            my_dict["suits"] = len(suits)
            all_dicts.append(my_dict)
        return all_dicts

    def evaluate_hand(self, hand_dict): 
        l = list(hand_dict["ranks"].items())
        if hand_dict['suits'] == 1:
            if 'T' in hand_dict['ranks'] and 'J' in hand_dict['ranks'] and 'Q' in hand_dict['ranks'] and 'K' in hand_dict['ranks'] and 'A' in hand_dict['ranks']:
                return 'Royal flush' #we already know suits == 1, jump to flush instead of four of a kind and full house
            if (rank_values[l[4][0]]-rank_values[l[0][0]] == 4) or (rank_values[l[4][0]]-rank_values[l[0][0]] == 12):
                return "Straight flush" 
            return "Flush"
        if l[0][1] == 4:  #most common rank occurs 4 times
            return "Four of a kind" 
            #full house: length ranks = 2, first value = 3
        if len(l) == 2:
            return "Full house"
        if len(l) == 5:
            if (rank_values[l[4][0]]-rank_values[l[0][0]] == 4) or (rank_values[l[4][0]]-rank_values[l[0][0]] == 12):
                return "Straight"
            return "Card high"
        if len(l) == 3:
            if l[0][1] == 3:
                return "Three of a kind"
            return "Two pair"
        if l[0][1] == 2:
            return "Pair"


#This will look at all of the players' hands, the individual hands, and the rank of each. This is for comparison later on to see who wins
#The cards will be ordered from lowest to highest. 

    
"""  


#Setting up the game
"""
#Players are identified, the deck is created and shuffled, and the table is formed
Millie = Player("Millie")
James = Player("James")
Bob = Player("Bob")

my_deck = Deck()
my_deck.shuffle_deck()

my_table = Table()

my_table.add_player(Millie)
my_table.add_player(James)
my_table.add_player(Bob)

print(my_table.players)

#The cards are dealt to the players and the 5 community cards are placed on the table
for i in range(2):
    for player in my_table.players:
        next_card = my_deck.deal_card()
        player.take_card(next_card)
for i in range(5):
    next_card = my_deck.deal_card()
    my_table.community_cards.append(next_card)

#The game has now been set

print(Millie.hand)
print(my_table.community_cards)

#form your hands and ranks

millie_hands = my_table.form_hands(Millie)
print(millie_hands)


millie_evaluated = [my_table.evaluate_hand(hand) for hand in millie_hands]
print(millie_evaluated)
"""



def evaluate_hand(hand_dict): 
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
        return "Card high"
    if len(l) == 3:
        if l[0][1] == 3:
            return "Three of a kind"
        return "Two pair"
    if l[0][1] == 2:
        return "Pair"


h = {"ranks": {"2":1, "3":1, "4":1, "5":1, "A":1, }, "suits":3}



print(evaluate_hand(h))
#for straight flush 
#2 3 4 5 A. if last is ace and second to last is 5, the suits are all the same so we cant have repeats. 
l = list(h["ranks"].items())
print(l)
print(l[4][0])
print(l[3][0])







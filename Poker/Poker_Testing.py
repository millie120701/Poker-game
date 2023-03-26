rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def form_hands(hands):
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
        #The ranks are sorted 
		sorted_ranks = sorted(ranks, key=lambda x: (ranks[x] == 1, rank_values[x])) 
		my_dict["ranks"] = {rank: ranks[rank] for rank in sorted_ranks}
        # suit total is calculated
		my_dict["suits"] = len(suits)
		#each dict added (each hand added)
		all_dicts.append(my_dict)
	return all_dicts


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



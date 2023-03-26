from Poker_Testing import form_hands, evaluate_hand
from poker_evaluation_bot import evaluate_hand_bot
from time import time 

rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
hand_ranks = {'Card high': 1, 'Pair': 2, 'Two pair':3, "Three of a kind" : 4, "Straight": 5, "Flush": 6, "Full house":7, "Four of a kind":8, "Straight flush":9, "Royal Flush":10}

from Poker_test_cases import possible_hands, flushes, high_cards, straights #every hand from txt file 


#Bot
'''
start_time = time()

for hand in possible_hands:
	evaluate_hand_bot(hand)

end_time = time()

duration1 = end_time - start_time


'''



hands_dict = form_hands(possible_hands)

for hand in hands_dict:
	print(evaluate_hand(hand))







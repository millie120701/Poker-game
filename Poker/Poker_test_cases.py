import random

poker_file = open("/Users/milliegallacher/Wordle/pokerhands.txt", "r")
poker_hands = poker_file.read()


#first value = suit
#second value = rank A is 1
#last value = hand type, index 10 

suits = {1: "H", 2: "S", 3: "C", 4 : "D"} #index 0, 2, 4, 6, 8
ranks = {1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "T", 11: "J", 12: "Q", 13: "K"} #indexes 1, 3, 5, 7, 9

split_hands = poker_hands.splitlines()
str_unsorted_hands = [line.split(",") for line in split_hands]
unsorted_hands = [[int(num) for num in hand] for hand in str_unsorted_hands]

def get_hand(hand):
	new_hand = []
	for i in range(0,10,2):
		new_card = ""
		new_card += ranks[hand[i+1]]
		new_card += suits[hand[i]]
		new_hand.append(new_card)
	return new_hand

high_card = []
one_pair = []
two_pair = []
three_of_a_kind = []
straight = []
flush = []
full_house = []
four_of_a_kind = []
straight_flush = []
royal_flush = []

for hand in unsorted_hands:
	if hand[-1] == 0:
		high_card.append(hand)
	elif hand[-1] == 1:
		one_pair.append(hand)
	elif hand[-1] == 2:
		two_pair.append(hand)
	elif hand[-1] == 3:
		three_of_a_kind.append(hand)
	elif hand[-1] == 4:
		straight.append(hand)
	elif hand[-1] == 5:
		flush.append(hand)
	elif hand[-1] == 6:
		full_house.append(hand)
	elif hand[-1] == 7:
		four_of_a_kind.append(hand)
	elif hand[-1] == 8:
		straight_flush.append(hand)
	else:
		royal_flush.append(hand)


possible_hands = []
for hand in unsorted_hands:
	possible_hands.append(get_hand(hand))

high_cards = []
for hand in high_card:
	high_cards.append(get_hand(hand))


flushes = []
for hand in flush:
	flushes.append(get_hand(hand))

straights = []
for hand in straight:
	straights.append(get_hand(hand))








h = ["JD", "TD", "QD", "KD", "AD"]

from operator import itemgetter

card_order = lambda x: "23456789TJQKA".index(x[0])
hand = [sorted(h, key = card_order)]



#For the first comparison (card one and two) we have possible outcomes as a result

#suit is the same
#cannot have full house (cannot have two cards of the same suit and rank next to eachother)
same_suit = ["Card high", "pair", "two pair", "three of a kind", "straight", "flush", "four of a kind", "straight flush", "royal flush"]

#suit is different
#cannot have flush, straight flush or royal flush
different_suit = ["Card high", "pair", "two pair", "three of a kind", "straight", "full house", "four of a kind"] 

#rank is the same 
#cannot have straight, flush (would require same suit which would make the cards identical), straight flush, royal flush
same_rank = ["pair", "two pair", "three of a kind", "full house", "four of a kind"]

#rank is different

different_rank = ["Card high", "pair", "two pair", "three of a kind", "straight", "flush", "full house", "four of a kind", "straight flush", "royal flush"]

#cant have same rank, same suit as this would be a repeat of the same card
#same_suit - different_rank(1) or different_suit - different_rank(2), same_rank - different-suit (3)
#The possible outcomes for 1, 2 and 3 are:

print(different_rank)
same_suit_different_rank = [element for element in same_suit if element in different_rank]
different_suit_different_rank = [element for element in different_suit if element in different_rank]
different_suit_same_rank = [element for element in different_suit if element in same_rank]
#print(same_suit_different_rank) #no deletions 
#print(different_suit_different_rank)
#print(different_suit_same_rank)

"""
What if you ordered the hand based on commonality?

- A card may trap two pairs:
If ordered on commonality, you will have 22665 instead of 22566. 
That way, you are not forced to evaluate the last card.

- This also goes for 4 of a kind:
The four of a kind will be at the beginning and together, you won't have to
evaluate the last card, if 33332 (would be 23333 the ordered way)

- If two cards are the same rank they cannot be the same suit:
With 23556, you may get tricked into thinking it could be a straight or a flush, with 
a pair as a possibility, but unsure.
if ordered like 55263, you know instantly there isn't a straight (nor a flush), 
and that you definitely have at least a pair

- General idea
If ordered just numerically, not count, you are forced to look at the rank/flush
of another card unnecessarily.
Again,for 23556, you see the 2,3 and think it may be a straight if the suits are the different,
or a flush/straight flush if the suits are the same.

You then have to look in two directions:
What if the suit is the same?
What if the suit is different?

If ordered like 55263, you know instantly it is not a straight, nor a flush. You see the pair, 
and also know they are different suits, so you don't have different routes depending on 
suit. You don't have to check the suit either, which saves time.


"""

bam = ['7H', 'TD', '2D', '7S', '2D']
def order_poker_hand(hand):
  counts = {}
  for card in hand:
    rank = card[0]
    if rank in counts:
      counts[rank] += 1
    else:
      counts[rank] = 1
  ordered_hand = []
  for rank in sorted(counts, key=lambda x: (-counts[x], x)):
    for i in range(counts[rank]):
      for card in hand:
        if card[0] == rank:
          ordered_hand.append(card)
          hand.remove(card)
          break
  return ordered_hand

print(order_poker_hand(bam))


"""
if card after is not the same rank, we have no pairs:
card high, straight, flush, straight flush, royal flush

if the card after is the same rank:
card high, pair, two pair, three of a kind, full house, four of a kind
-----------

we can check suit at the same time, for the first round we check suit and rank

ROUND ONE
---------
- Suit same, rank same: CANNOT OCCUR

- Suit same, rank not same: (5) ONE
card high, flush, straight flush, royal flush 

- Suit different, rank same: (5) TWO
pair, two pair, three of a kind, full house, four of a kind, 

- suit different, rank different THREE
card high, straight (2)

ROUND TWO
---------
We can now go through both individually, especially with the lower possibilities now.

Hand ONE: (suit same, rank same) 
We know that there are no pairs so we do not have to look if the rank is the same
CHECK ROYAL FLUSH FIRST
rf = ["T", "J", "Q", "K", "A"]

my_hand = ["T", "J", "Q", "K", "A"]

for i in range(5):
	if my_hand[i] != rf[i]:
		print(False)
		break
print(True)

IF NOT:
- suit same rank not same
card high, flush, straight flush
- suit different, rank not same ENDS
card high

Hand TWO (suit different, rank same)
We know that a flush isnt possible so any suit info is useless.
- rank not same (rules out three of a kind and four of a kind)
pair, two pair, full house 
- rank same: (we find out that there is at least three of a kind)
three of a kind, full house, four of a kind

Hand THREE (suit diff rank diff) ENDS
We either have card high or straight. We know that the first two cards are different ranks,
and there are no pairs. Therefore, if the first card is 4 higher than the last card
then it is a straight, as no repeats are affecting the count from start to finish.

ROUND THREE
-----------
We have three hands left to evaluate. 
HAND ONE:
One hand
HAND TWO:
Two hands
HAND THREE:
no hands



- Suit same, rank not same: (5) ONE
card high, flush, straight flush, royal flush 
best way would be to loop through the royal flush hand, because chances of a royal flush
are LOW and it would break the loop as soon as it isn't true. Rather than comparing
the whole hand.




rf = ["T", "J", "Q", "K", "A"]

my_hand = ["AH", "KH", "QH", "JH", "TH"]

for i in range(5):
	if my_hand[i][] != rf[i]:
		print(False)
		break
print(True)








for each hand you could have a dict,
ranks and how many of each

suits: if you one suit you know it's flush, straight flush, royal flush

{ranks: {A:2, J:3}, suits: {hearts: 2, spades: 2, diamonds: 1}}

Ahearts Aspades, Jhearts, Jspades, Jdiamonds

full house.

{ranks: {T:1, J:1, Q:1, K:1, A:1}, suits: {spades:1}}

Do first, check for royal flush, suit must be 1, ranks must begin with T, then J etc
if we find any reason to break, we break the loop. we also find information by doing this
if the first rank isn't 10 and suits > 1. we already cut out flushes and royal flush.

so we should order the ranks in commonality, but if no commons or commons have passed then in order. 
evaluate suits and ranks.


This method seems reasonable at the moment.

SUITS - we need to expose the program to suits == 1 first because of the royal flush.
suits == 1 
at least got a flush,
POSSIBILITIES
flush, straight flush, royal flush
Now compare the first and last values.
we CAN'T have any pairs.
first check the royal flush, is the first card a 10? if it is, is the last card an A?
if the first card is not a 10, see what the first card is and what the last card is for straight flush.
If the last and first card are not 4 apart, it is just a regular flush. 

ENDS, 



SUITS 
suits >1
This eliminates any flushes
POSSIBILITIES
card high, pair, two pair, three of a kind, straight, full house, four of a kind
VALUES
if first value == 4:
	four of a kind (best hand found)

if first value == 3:
	three of a kind, or full house
is the next value a 2? if yes full house, if no, three of a kind. 

if first value == 2:
	pair or two pair
	if next = 2 then two pair

if first value == 1:
	card high or straight ?? straight should be found earlier on than this




- these need to be found in importance, so first is four of a kind, we need the first key to be 4.

- card high, pair, two pair, three of a kind, straight, full house, four of a kind 

if so, we know it is four of a kind

---------
if value = 4: four of a kind
if 3:
	2 would be full house
	1 would be three of a kind

now we have straight, two pair, one pair, and high left

if last and first are 4 apart (list is ordered): straight

two pair, one pair and high left:
if first value == 2, if next is 1 then one pair
if next is 2 then two pair

else: card high.



value orders:
full house would be 3, 2, 1
three of a kind would be 3, 1, 1 
straight: 1, 1, 1, 1, 1 (order, first last are same)
two pair: 2, 2, 1
one pair: 2, 1, 1, 1, 1
high: 1, 1, 1, 1, 1 (not ordered)


suit poss:
straight: 2, 4 (should be above three of a kind really.)
two pair: 4, 2
one pair: 2, 4 
high: 2, 4

"""


def evaluate_hand_bot(hand):
  # Step 1: Create a dictionary to count the frequency of each card value
  values = {}
  for card in hand:
    value = card[0]
    if value in values:
      values[value] += 1
    else:
      values[value] = 1

  # values = {"2":1, "T":1, "K":2, "Q":1}
  
  # Step 2: Check for pairs, three of a kind, and four of a kind
  has_pair = False
  has_three_of_a_kind = False
  has_four_of_a_kind = False
  has_two_pair = False

  card_values = list(values.values())

  try:
  	card_values.remove(2) # -> May throw ValueError
  	card_values.remove(2) # -> May throw ValueError
  	has_two_pair = True
  except ValueError:
  	has_two_pair = False

  for value, count in values.items():
    if count == 2:
      has_pair = True
    elif count == 3:
      has_three_of_a_kind = True
    elif count == 4:
      has_four_of_a_kind = True
  
  # Step 3: Check for a flush
  suits = [card[1] for card in hand]
  has_flush = all(suit == suits[0] for suit in suits)

  # A2345
  # TJQKA

  # returns the index of X in our custom-ordered string
  card_order = lambda x: "23456789TJQKA".index(str(x).upper())
  
  # Step 4: Check for a straight
  values = sorted([card[0] for card in hand], key=card_order)
  has_straight = values in [["A", "2", "3", "4", "5"], ["T", "J", "Q", "K", "A"]] or all(card_order(values[i]) == card_order(values[i-1]) + 1 for i in range(1, len(values)))
  
  # Step 5: Determine the rank of the hand
  if has_straight and has_flush:
    if values == ["T", "J", "Q", "K", "A"]:
        return "Royal Flush"
    else:
  	    return "Straight Flush"
  elif has_four_of_a_kind:
    return "Four of a Kind"
  elif has_three_of_a_kind and has_pair:
    return "Full House"
  elif has_flush:
    return "Flush"
  elif has_straight:
    return "Straight"
  elif has_three_of_a_kind:
    return "Three of a Kind"
  elif has_two_pair:
  	return "Two Pair"
  elif has_pair:
    return "One Pair"
  else:
    return "High Card"

# Test the function
hands = {
"High Card":       ["2H", "3C", "4D", "5C", "7S"],
"One Pair":        ["2H", "2S", "4D", "5C", "7S"],
"Two Pair":        ["2H", "2S", "4D", "4C", "7S"],
"Three of a Kind": ["2H", "2S", "2D", "5C", "7S"],
"Straight":        ["AH", "2S", "3D", "4C", "5S"],
"Straight":        ["2H", "3S", "4D", "5C", "6S"],
"Straight":        ["5H", "6S", "7D", "8C", "9S"],
"Straight":        ["5H", "8S", "7D", "6C", "9S"],
"Straight":        ["8H", "9S", "TD", "JC", "QS"],
"Straight":        ["TH", "JS", "QD", "KC", "AS"],
"Flush":           ["2H", "5H", "7H", "9H", "JH"],
"Full House":      ["2H", "2S", "2D", "5C", "5S"],
"Four of a Kind":  ["2H", "2S", "2D", "2C", "5S"],
"Straight Flush":  ["2H", "3H", "4H", "5H", "6H"],
"Royal Flush":     ["TH", "JH", "QH", "KH", "AH"]}





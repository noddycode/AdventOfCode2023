# First thing I notice is that we can pretty easily optimize things with our friend; sets!
#     Five of a kind, where all five cards have the same label: AAAAA
#     Four of a kind, where four cards have the same label and one card has a different label: AA8AA
#     Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
#     Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
#     Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
#     One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
#     High card, where all cards' labels are distinct: 23456
# So right away, if we convert each hand to a set, we can figure out several of these by length
# len == 1: Five of a kind
# len == 2: Four of a kind, Full House
# len == 3: Three of a kind, two pair
# len == 4: One pair
# len == 5: high card
# Using this, we can quickly narrow down which hand we have
# For the tiebreaker, we can then count how many of each we have
from functools import total_ordering

# This class will allow us to simply sort our input
@total_ordering
class Card:
	# we'll convert every card to a number for simplicity
	# Doesn't really matter what the value itself is
	CARD_VALUES = {c:i for i, c in enumerate('23456789TJQKA')}

	def __init__(self, hand):
		self.cards = [self.CARD_VALUES[c] for c in hand]

	def getHandRank(self):
		unique_cards = set(self.cards)
		if len(unique_cards) == 1:
			return 7
		elif len(unique_cards) == 2:  # full house, four of a kind
			# Four of a kind
			if any(self.cards.count(v) == 4 for v in unique_cards):
				return 6
			else:  # Full house
				return 5
		elif len(unique_cards) == 3:  # two pair, three of a kind
			# Three of a kind
			if any(self.cards.count(v) == 3 for v in unique_cards):
				return 4
			else:  # Two pair
				return 3
		elif len(unique_cards) == 4:  # one pair
			return 2
		elif len(unique_cards) == 5:  # high card
			return 1

	def __gt__(self, other):
		if self.getHandRank() != other.getHandRank():
			return self.getHandRank() > other.getHandRank()

		for my_card, other_card in zip(self.cards, other.cards):
			if my_card != other_card:
				return my_card > other_card

	def __eq__(self, other):
		return self.getHandRank() == other.getHandRank() and self.cards == other.cards

	def __repr__(self):
		return str(self.cards)

hand_bids = []
with open('input.txt') as fin:
	for line in fin:
		hand, bid = line.split()
		hand_bids.append((Card(hand), int(bid)))

hand_bids = sorted(hand_bids, key=lambda x: x[0])
bid_values = [b * (i+1) for i, (_, b) in enumerate(hand_bids)]

print(hand_bids)
print(sum(bid_values))




from functools import total_ordering

@total_ordering
class Card:
	# we'll convert every card to a number for simplicity
	# Doesn't really matter what the value itself is
	CARD_VALUES = {c:i for i, c in enumerate('J23456789TQKA')}

	def __init__(self, hand):
		self.hand = hand
		self.cards = [self.CARD_VALUES[c] for c in hand]

	def getHandRank(self):
		# Let's think about this
		# How do we know what card the joker needs to be?
		# Well, let's take our examples
		# T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
		# Is it safe to just convert any jokers to whichever card there are the most of?
		# Let's try it

		unique_cards = set(self.cards)
		card_counts = [(c, self.cards.count(c)) for c in unique_cards if c != 0]
		if unique_cards == {0}:
			# Corner case we have to handle for all Jokers
			# We can substitute any card, the value of the card doesn't matter
			max_card = 1
		else:
			max_card = sorted(card_counts, key=lambda x: x[1], reverse=True)[0][0]
		compare_cards = [max_card if c == 0 else c for c in self.cards]

		unique_cards = set(compare_cards)
		if len(unique_cards) == 1:
			return 7
		elif len(unique_cards) == 2:  # full house, four of a kind
			# Four of a kind
			if any(compare_cards.count(v) == 4 for v in unique_cards):
				return 6
			else:  # Full house
				return 5
		elif len(unique_cards) == 3:  # two pair, three of a kind
			# Three of a kind
			if any(compare_cards.count(v) == 3 for v in unique_cards):
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
		return self.hand

hand_bids = []
# https://www.reddit.com/r/adventofcode/comments/18cr4xr/2023_day_7_better_example_input_not_a_spoiler/
with open('edge_case_input.txt') as fin:
	for line in fin:
		hand, bid = line.split()
		hand_bids.append((Card(hand), int(bid)))

hand_bids = sorted(hand_bids, key=lambda x: x[0])
bid_values = [b * (i+1) for i, (_, b) in enumerate(hand_bids)]

print(hand_bids)
print(sum(bid_values))




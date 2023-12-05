# My brain is already melting
# We'll use a dictionary to keep track of how many we have of each card
from collections import defaultdict

cards = defaultdict(int)

with open('input.txt') as fin:
	# Get the last card number so we don't go past it
	last_card_number = int(fin.readlines()[-1].split()[1].strip(':'))
	fin.seek(0)

	for line in fin:
		card_number = int(line.split()[1].strip(':'))
		cards[card_number] += 1 # We always have at least one of each card
		card = line.split(':')[1]
		winning_numbers = {int(n.strip()) for n in card.split('|')[0].split()}
		scratched_numbers = {int(n.strip()) for n in card.split('|')[1].split()}

		matched = winning_numbers.intersection(scratched_numbers)

		# Keep track of how many we have of each card
		if matched:
			for _ in range(cards[card_number]):
				# Card 2: 3 Winning Numbers
				# So we get a copy of cards 3, 4, and 5
				# That would be a range from 3-5
				# So range would start at card_number + 1 (2+1)
				# And end at card_number + len(matched) (2+3)
				# +1 cause range exclusive
				for i in range(card_number+1, card_number+len(matched)+1):
					if i > last_card_number:
						break
					cards[i] += 1


print(cards)
print(sum(cards.values()))

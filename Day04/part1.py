# I know a use case for sets when I see one

sum = 0
with open('input.txt') as fin:
	for line in fin:
		card = line.split(':')[1]
		winning_numbers = {int(n.strip()) for n in card.split('|')[0].split()}
		scratched_numbers = {int(n.strip()) for n in card.split('|')[1].split()}

		matched = winning_numbers.intersection(scratched_numbers)

		# What's the math of this?
		# 3 winning numbers = (1)*2*2 = 4
		# 4 winning numbers = (1)*2*2*2 = 8
		# 5 winning numbers = (1)*2*2*2*2 = 16
		# We can disregard the 1 cause it's all a product
	  # So that's 2^(n-1)
		# (even works for 1 winning number cause anything ^0 = 1)

		if matched:
			sum += 2**(len(matched) - 1)

print(sum)

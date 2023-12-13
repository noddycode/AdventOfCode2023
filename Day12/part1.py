import re

springs = []
with open('sample.txt') as fin:
	for line in fin:
		line = line.strip()
		spring_line, ranges = line.split()
		ranges = (int(r) for r in ranges.split(','))
		springs.append((spring_line, ranges))

# For now, let's brute force this and see if we can spot any patterns
num_variations = []
for spring, ranges in springs:
	# First we'll generate all the complete subtrings we should see in an undamaged map
	range_substrings = {i: '#' * r for i,r in enumerate(ranges)}

	temp_spring = spring
	found_substrings = set()
	# We'll start with the biggest substring and work our way down
	# We want to find all the substrings that match the ranges exactly
	full_ranges = re.split(r'[^#]', spring)
	for index, spring_range in sorted(range_substrings.items(), key=lambda x: (len(x[1]), -x[0]), reverse=True):
		if spring_range in full_ranges and all(index > fs for fs in found_substrings):
			found_substrings.add(index)
			temp_spring = temp_spring.replace(spring_range, str(index), 1)

	# range_substrings = [(i, '#' * r) for i,r in enumerate(ranges) if i not in found_substrings]
	# for index, spring_range in range_substrings:
	remaining_ranges = temp_spring.split('$')
	print(remaining_ranges)




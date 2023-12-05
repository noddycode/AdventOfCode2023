from itertools import groupby
powers = []
with open('input.txt') as fin:
	for line in fin:
		line = line.lower().strip()
		game_number = int(line.split()[1].strip(':'))
		pulls = line.split(':')[1].split(';')

		pair_values = []
		for pull in pulls:
			pairs = pull.split(',')
			for pair in pairs:
				num_cubes, color = [p.strip() for p in pair.split()]
				num_cubes = int(num_cubes)

				pair_values.append((num_cubes, color))

		# Let's use groupby cause I'm pretty bad at it
		# First, we have to sort because that's what groupby expects
		pair_values = sorted(pair_values, key=lambda x: x[1])
		# Now we can group by color
		power = 1
		for color, group in groupby(pair_values, key=lambda x: x[1]):
			# Gives us the max number of cubes for each color
			power *= max(g[0] for g in group)

		powers.append(power)

print(powers)
print(sum(powers))






from itertools import combinations

# Okay... that was a bit more of a leap than I was expecting
# But if we think about it, we don't actually need to maintain the map
# We just need to figure out how much space gets added between galaxies
# Well, we know where all the galaxies are
# And the empty rows and columns
# So I think we can just check if each galaxy is before/after an empty row/column

starmap = []
galaxy_points = {}
empty_rows = []
empty_columns = []
# Have to account for existing row
growth_factor = 999999
with open('input.txt') as fin:
	for i, line in enumerate(fin):
		line = line.strip()
		for j, char in enumerate(line):
			if char == '#':
				galaxy_points[(j, i)] = len(galaxy_points)+1
		starmap.append(list(line))
		if len(set(line)) == 1 and '.' in line:
			empty_rows.append(i)

# Get all empty map columns
for i in range(len(starmap[0])):
	column_chars = {row[i] for row in starmap}
	if len(column_chars) == 1 and '.' in column_chars:
		empty_columns.append(i)

def get_adjusted_coordinates(point):
	x, y = point
	yoffset = 0
	xoffset = 0
	for row in empty_rows:
		if y > row:
			yoffset += 1
	for column in empty_columns:
		if x > column:
			xoffset += 1

	return x + xoffset * growth_factor, y + yoffset * growth_factor

def get_manhattan_distance(point1, point2):
	# Now update this to count the disance between galaxies

	x1, y1 = get_adjusted_coordinates(point1)
	x2, y2 = get_adjusted_coordinates(point2)
	return abs(x1 - x2) + abs(y1 - y2)

galaxy_dists = {}
# The shortest distance will automatically be the manhattan distance
# We'll use collections to help
for pair in combinations(galaxy_points.keys(), 2):
	galaxy_numbers = (galaxy_points[pair[0]], galaxy_points[pair[1]])
	# We'll use the universe numbers for debugging
	galaxy_dists[galaxy_numbers] = get_manhattan_distance(*pair)

total = sum(galaxy_dists.values())
print(total)

print(galaxy_points)
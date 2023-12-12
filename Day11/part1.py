# So two things immediately spring to mind
# 1) This is def gonna be like "do 100 years of this" or something, so manually expanding the
# grid manually isn't gonna help. However, we'll do it anyway and see if we can spot some useful patterns
# 2) We'll need to find "manhattan" distance. There's a formula out there somewhere we can use I'm sure
from itertools import combinations

starmap = []
galaxy_points = {}
empty_rows = []
empty_columns = []
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


def get_manhattan_distance(point1, point2):
	# This is actually a pretty simple formula
	# https://www.omnicalculator.com/math/manhattan-distance
	x1, y1 = point1
	x2, y2 = point2
	return abs(x1 - x2) + abs(y1 - y2)

def get_all_galaxies():
	global galaxy_points
	galaxy_points = {}
	for i, row in enumerate(starmap):
		for j, char in enumerate(row):
			if char == '#':
				galaxy_points[(j, i)] = len(galaxy_points)+1

def expand_universe():
	# Handle rows first
	for offset, row in enumerate(empty_rows):
		# Offset keeps track of our row as we add new rows
		new_row = list('.' * len(starmap[0]))
		starmap.insert(row + offset, new_row)

	# Now handle columns
	for offset, column in enumerate(empty_columns):
		for row in starmap:
			row.insert(column + offset, '.')

	get_all_galaxies()

def print_map():
	curr_galaxy = 1
	for row in starmap:
		for i,char in enumerate(row):
			if char == '#':
				row[i] = str(curr_galaxy)
				curr_galaxy += 1

		print(''.join(row))
	print()


expand_universe()
print_map()

galaxy_dists = {}
# The shortest distance will automatically be the manhattan distance
# We'll use collections to help
for pair in combinations(galaxy_points.keys(), 2):
	galaxy_numbers = (galaxy_points[pair[0]], galaxy_points[pair[1]])
	# We'll use the universe numbers for debugging
	galaxy_dists[galaxy_numbers] = get_manhattan_distance(*pair)

print(sum(galaxy_dists.values()))
print(galaxy_points)
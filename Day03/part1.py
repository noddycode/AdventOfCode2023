from collections import namedtuple
from itertools import groupby
# This is a doozy...
# Usually I'd have a function to get all adjacent cells
# But I'm not sure how to combine that with getting the numbers...
# Could we maybe get the numbers first?
# This being Day 3 makes me feel like there's a fairly simple way to do this

# So let's say we parse all of the numbers first
# We store their row, starting column index, and ending column index
# Then we can use our adjacent cell function
# And check all indices in that range
# It won't be efficient but... who cares

ParsedNumber = namedtuple('ParsedTuple', ('number', 'row', 'columns'))
parsed_numbers: list[ParsedNumber] = []

schematic = []

def add_parsed_number(number: str, row: int, index: int):
	# Handy thing keeps us from having to store the starting index
	# +1 here because the length includes the index we're on
	# Say a three-digit number ends at index 8
	# ......123...
	# The index of the last digit, 3, is at index 8
	# So we only go back 2 indices to get the starting index
	starting_index = index - (len(number)) + 1

	parsed_numbers.append(ParsedNumber(
		number=int(number),
		row=row,
		columns=(starting_index, index)
	))


with open('input.txt') as fin:
	schematic = [line.strip() for line in fin]


for row, line in enumerate(schematic):
	line = line.strip()
	curr_number = ""
	for index, c in enumerate(line):
		if c.isdigit():
			curr_number += c
		else:
			if curr_number:
				# We subtract one here because the index passed in is one PAST the end of the number
				# Recall that we only add the number after we've parsed the next character
				add_parsed_number(curr_number, row, index-1)
				curr_number = ""

	# Always have to clean up the last character
	if curr_number:
		# Remember that these values exist outside of the for loop
		add_parsed_number(curr_number, row, index)


# For debugging purposes
def render_adjacent_cells(adjacent):
	render = []
	# Sort these for groupby so we don't have to pre-name our matrix
	sorted_adjacent = sorted(adjacent, key=lambda x: x[0])
	for row, group in groupby(sorted_adjacent, key=lambda x: x[0]):
		if row < 0 or row >= len(schematic):
			continue
		render_row = []
		for column in [g[1] for g in group]:
			if column < 0 or column >= len(schematic[row]):
				continue
			render_row.append(schematic[row][column])
		render.append(render_row)

	print('-------------')
	for row in render:
		print(''.join(row))
	print('-------------')

def get_adjacent_cells(parsed: ParsedNumber):
	adjacent = []
	# +2 here because range is exclusive on the right
	for row in range(parsed.row - 1, parsed.row + 2):
		for column in range(parsed.columns[0] - 1, parsed.columns[1] + 2):
			adjacent.append((row, column))

	render_adjacent_cells(adjacent)

	return adjacent

part_numbers = []
# Now we can check all cells next to our numbers
for parsed in parsed_numbers:
	adjacent_cells = get_adjacent_cells(parsed)
	for row, column in adjacent_cells:
		if row < 0 or row >= len(schematic):
			continue
		if column < 0 or column >= len(schematic[row]):
			continue

		if (not schematic[row][column].isdigit()) and schematic[row][column] != ".":
			part_numbers.append(parsed.number)


print({p.number for p in parsed_numbers} - set(part_numbers))
print(part_numbers)
print(sum(part_numbers))
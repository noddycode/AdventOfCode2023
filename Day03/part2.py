from collections import namedtuple, defaultdict
from itertools import groupby

ParsedNumber = namedtuple('ParsedTuple', ('number', 'row', 'columns'))
parsed_numbers: list[ParsedNumber] = []

schematic = []

# This part can all stay the same
def add_parsed_number(number: str, row: int, index: int):
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
				add_parsed_number(curr_number, row, index-1)
				curr_number = ""

	if curr_number:
		add_parsed_number(curr_number, row, index)


def get_adjacent_cells(parsed: ParsedNumber):
	adjacent = []
	# +2 here because range is exclusive on the right
	for row in range(parsed.row - 1, parsed.row + 2):
		for column in range(parsed.columns[0] - 1, parsed.columns[1] + 2):
			adjacent.append((row, column))

	return adjacent

# Here we will store every index we find containing "*"
# In the end, we can filter it to only the ones that have exactly two numbers in their list

possible_gears = defaultdict(list)
for parsed in parsed_numbers:
	adjacent_cells = get_adjacent_cells(parsed)
	for row, column in adjacent_cells:
		if row < 0 or row >= len(schematic):
			continue
		if column < 0 or column >= len(schematic[row]):
			continue

		# Thankfully this is really the only thing we have to change
		if schematic[row][column] == '*':
			possible_gears[(row, column)].append(parsed.number)

sum = 0

for numbers in possible_gears.values():
	if len(numbers) == 2:
		sum += numbers[0] * numbers[1]

print(sum)
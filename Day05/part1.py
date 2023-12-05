from enum import Enum


# Okay, this one is a little complex
# To simplify parsing, let's first assign enums to each map part

class Part(Enum):
	SEED = 0
	SOIL = 1
	FERTILIZER = 2
	WATER = 3
	LIGHT = 4
	TEMP = 5
	HUMIDITY = 6
	LOCATION = 7

# I don't think we really need to map every seed to a location
# We only need to care about our starting seeds
# I think we can use those as our inputs and simply go down the maps looking for a match for each one

# First we need to get our data into something usable

with open('sample_input.txt') as fin:
	text = fin.read()
	maps = text.split('\n\n')

seeds = [int(s) for s in maps[0].split(':')[1].split() if s]

# We don't really need to care what map maps to what, we know they're in order
# So we can just use a list of lists
seed_maps = []
for map in maps[1:]:
	lines = map.split('\n')
	ranges = []
	# First line is just the map name and tbh we don't care
	for line in lines[1:]:
		dest, source, range_num = [int(n) for n in line.split()]
		range_num -= 1 # Our range includes the starting value already
		# We'll leave them as ranges so we can lazy load them as needed
		ranges.append(((dest, dest + range_num), (source, source + range_num)))

	seed_maps.append(ranges)

# Now we just recurse down through these ranges for each seed
def get_map_value(initial_value, map_index):
	# We've reached the end of the maps, so we're done
	if map_index == len(seed_maps):
		return initial_value

	for dest_range, source_range in seed_maps[map_index]:
		if source_range[0] <= initial_value <= source_range[1]:
			# Now that we know our range, we can calculate the new value
			# Okay, so if our value is 3 and we're in the range 2-5
			# 2, 3, 4 ,5
			pass


	get_map_value(initial_value, map_index + 1)


for seed in seeds:
	print(get_map_value(seed, 0))
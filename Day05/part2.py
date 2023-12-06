# Okay so checking every seed is not the answer
# But we KNOW we want the lowest location
# And we know all the locations
# Let's just use the lowest location we have
# We can kinda cheat like this cause we know there's a location 0
with open('input.txt') as fin:
	text = fin.read()
	maps = text.split('\n\n')

seeds = [int(s) for s in maps[0].split(':')[1].split() if s]

seed_maps = []
for map in maps[1:]:
	lines = map.split('\n')
	ranges = []
	for line in lines[1:]:
		dest, source, range_num = [int(n) for n in line.split()]
		range_num -= 1
		ranges.append(((dest, dest + range_num), (source, source + range_num)))

	seed_maps.append(ranges)

def get_seed_value(initial_value, map_index):
	if map_index < 0:
		return initial_value

	# Just flip everything around
	for source_range, dest_range in seed_maps[map_index]:
		if source_range[0] <= initial_value <= source_range[1]:
			ix = initial_value - source_range[0]
			mapped_value = dest_range[0] + ix
			return get_seed_value(mapped_value, map_index - 1)
	else:
		# If we didn't find the range, the value is 1:1
		return get_seed_value(initial_value, map_index - 1)

seed_ranges = []
for i in range(0, len(seeds), 2):
	seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))

# Let's hope this works
# It's not fast but it could be slower :)
location_num = 0
while True:
	seed_num = get_seed_value(location_num, len(seed_maps) - 1)
	if any(seed[0] <= seed_num <= seed[1] for seed in seed_ranges):
		print(location_num)
		break
	location_num += 1



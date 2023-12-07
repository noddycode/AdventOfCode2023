# Sod the algebra
# Simple observation shows us that simply windng for half the time gets decent results
# It seems like the distance is roughly parabolic so we'll just start there each time
# And then slowly go up and down until we go below the record

with open('input.txt') as fin:
	times = [int(t) for t in next(fin).split()[1:]]
	distances = [int(d) for d in next(fin).split()[1:]]

def get_distance(starting_wind, multplier, race_index):
	wind_time = starting_wind
	wind_times = []
	while True:
		wind_time += 1*multplier
		race_time = times[race_index] - wind_time
		distance = race_time * wind_time
		if distance > distances[race_index]:
			wind_times.append(wind_time)
		else:
			break

	return wind_times


product = 1
for i in range(len(times)):
	winning_times = []
	curr_wind = times[i] // 2
	winning_times.append(curr_wind)
	winning_times.extend(get_distance(curr_wind, 1, i))
	winning_times.extend(get_distance(curr_wind, -1, i))

	product *= len(winning_times)
	print(len(winning_times))


print(product)
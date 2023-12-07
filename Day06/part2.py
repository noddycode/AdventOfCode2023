# Brute force win every time

with open('input.txt') as fin:
	time = int(''.join(next(fin).split()[1:]))
	distance = int(''.join(next(fin).split()[1:]))

def get_distance(starting_wind, multplier):
	wind_time = starting_wind
	wind_times = []
	while True:
		wind_time += 1*multplier
		race_time = time - wind_time
		max_distance = race_time * wind_time
		if max_distance > distance:
			wind_times.append(wind_time)
		else:
			break

	return wind_times


product = 1
winning_times = []
curr_wind = time // 2
winning_times.append(curr_wind)
winning_times.extend(get_distance(curr_wind, 1))
winning_times.extend(get_distance(curr_wind, -1))

print(len(winning_times))
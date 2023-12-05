NUM_RED_CUBES = 12
NUM_GREEN_CUBES = 13
NUM_BLUE_CUBES = 14

possible_games = []
with open('input.txt') as fin:
	for line in fin:
		line = line.lower().strip()
		game_number = int(line.split()[1].strip(':'))
		pulls = line.split(':')[1].split(';')

		game_possible = True

		for pull in pulls:
			pairs = pull.split(',')
			for pair in pairs:
				num_cubes, color = [p.strip() for p in pair.split()]
				num_cubes = int(num_cubes)

				checks = (
						color.startswith('r') and num_cubes > NUM_RED_CUBES,
						color.startswith('g') and num_cubes > NUM_GREEN_CUBES,
						color.startswith('b') and num_cubes > NUM_BLUE_CUBES,
				)

				if any(checks):
					game_possible = False
					break

		if game_possible:
			possible_games.append(game_number)

print(possible_games)
print(sum(possible_games))







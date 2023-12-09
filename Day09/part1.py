inputs = []
with open('input.txt') as fin:
	for line in fin:
		inputs.append([int(n) for n in line.split()])

def extrapolate(diff_list, index, extrapolated_value):
	if index == 0:
		return extrapolated_value

	curr_row = diff_list[index]
	curr_row.append(extrapolated_value)

	above_row = diff_list[index-1]

	new_value = above_row[-1] + curr_row[-1]

	return extrapolate(diff_list, index - 1, new_value)



extrapolated_values = []
for values in inputs:
	difference_list = [values]
	last_diff = values
	while True:
		differences = []
		for i in range(len(last_diff) - 1):
			differences.append(last_diff[i + 1] - last_diff[i])

		difference_list.append(differences)
		last_diff = differences
		if len(set(differences)) == 1 and differences[0] == 0:
			value = extrapolate(difference_list, len(difference_list) - 1, 0)
			print(value)
			extrapolated_values.append(value)
			break

print(extrapolated_values)
print(sum(extrapolated_values))
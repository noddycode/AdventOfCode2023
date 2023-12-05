digits = []
number_strings = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'one', 'two', 'three', 'four', 'five', 'six',
									'seven', 'eight', 'nine', 'zero']
with open('input.txt') as fin:
	for line in fin:
		line = line.lower()
		# Returns the index of the substring so
		found_numbers = {(line.find(ns), ns) for ns in number_strings if line.find(ns) > -1}
		# Do this in case of duplicates. We really only care about the first and last instance
		found_numbers = found_numbers.union({(line.rfind(ns), ns) for ns in number_strings if line.find(ns) > -1})

		found_numbers = sorted(found_numbers, key=lambda x: x[0])

		numbers = []
		for index, number in found_numbers:
			if number.isdigit():
				numbers.append(number)
			else:
				# Saves us from having to make a dictionary
				converted = number_strings[number_strings.index(number) - 10]
				numbers.append(converted)

		digits.append(numbers[0] + numbers[-1])

print(sum(int(d) for d in digits))

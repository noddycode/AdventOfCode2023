digits = []
with open('input.txt') as fin:
	for line in fin:
		numbers = [d for d in line if d.isdigit()]
		digits.append(numbers[0] + numbers[-1])

print(sum(int(d) for d in digits))

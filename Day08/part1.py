tree = {}
with open('sample_input.txt') as fin:
	instructions = next(fin).strip()
	next(fin)
	for line in fin:
		node, children = line.split('=')
		node = node.strip()
		left, right = children.strip().strip('()').split(',')
		tree[node] = (left.strip(), right.strip())

print(tree)
curr_node = 'AAA'
count = 0
curr_instruction = 0
while True:
	instruction = instructions[curr_instruction]
	if instruction == 'L':
		curr_node = tree[curr_node][0]
	elif instruction == 'R':
		curr_node = tree[curr_node][1]

	count += 1

	if curr_node == 'ZZZ':
		break
	else:
		curr_instruction += 1
		if curr_instruction >= len(instructions):
			curr_instruction = 0

print(count)






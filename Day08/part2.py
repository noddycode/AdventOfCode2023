tree = {}
with open('input.txt') as fin:
	instructions = next(fin).strip()
	next(fin)
	for line in fin:
		node, children = line.split('=')
		node = node.strip()
		left, right = children.strip().strip('()').split(',')
		tree[node] = (left.strip(), right.strip())

# Obviously moving every map every time isn't going to work
# Let's try it this way...
# Let's start with each node and perform the algo until we end at an ending node
# We know we have to go at _least_ that far to get to the end
# Then we can proceed to the next node
# If we don't end up with a common one after that?
# I dunno, we'll burn that bridge when we get to it
# We'll also keep track of how many iterations we've done of the instructions
# So we can skip forward for the remaining nodes
starting_nodes = [n for n in tree.keys() if n.endswith('A')]

# Can we math it so we can skip counting the iterations?
# Modulo!
largest_count = 0
for node in starting_nodes:
	count = 0
	curr_node = node
	while True:
		# This will tell us where in the iterations we are without having to count them directly
		curr_instruction = count % len(instructions)
		instruction = instructions[curr_instruction]
		if instruction == 'L':
			curr_node = tree[curr_node][0]
		elif instruction == 'R':
			curr_node = tree[curr_node][1]

		count += 1

		if curr_node.endswith('Z'):
			largest_count = max(largest_count, count)
			break

print(largest_count)






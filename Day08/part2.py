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
counts = {}
for node in starting_nodes:
	count = 0
	curr_node = node
	curr_instruction = 0
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
			counts[node] = count
			break

# Now we know how many iterations it takes to get to each node
# What can we do with this information?
# We have to figure out how to line them all up
# https://stackoverflow.com/questions/19310482/javascript-function-to-multiply-two-numbers-until-they-equal-each-other
# So how do we apply this for all of our nodes?
# Let's loop over each node's count and multuply it until it's the highest
# And repeat this until they all match

largest_count = max(counts.values())
curr_counts = counts.copy()
done = False
while not done:
	for node, count in counts.items():
		curr_count = curr_counts[node]
		while curr_count < largest_count:
			curr_count += count

		# Let's be smarter
		# if curr_count < largest_count:
		# 	curr_count = count * (largest_count // count)
		# 	curr_count += count
		#
		# print(curr_count)

		largest_count = curr_count
		curr_counts[node] = curr_count

		# print(curr_counts.values())

		# Check if they're all even now
		if len(set(curr_counts.values())) == 1:
			done = True
			break


print(len(starting_nodes))
print(largest_count)






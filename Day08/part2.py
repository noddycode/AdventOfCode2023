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
# We know we have to repeat the instructions at least that many times
# To end up at the same place
# What can we do with this information?
# We have to figure out how to line them all up
# https://stackoverflow.com/questions/19310482/javascript-function-to-multiply-two-numbers-until-they-equal-each-other
# So how do we apply this for all of our nodes?
# Let's start at the lowest and work our way up

node_counts = sorted(counts.items(), key=lambda x: x[1])
curr_node = 0
curr_high = node_counts[1][1]
for i in range(len(node_counts)):
	lower = node_counts[i][1]

	curr = lower
	while True:
		curr += lower
		if curr % curr_high == 0 and curr % lower == 0:
			print(curr)
			break

	curr_high = curr
print(curr_high)

# Let's think about how this works
# So we have two numbers, 15 and 10
# We want to know how many times we need to loop these numbers to get them to be the same
# So we start with the lower number, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
# Then we do 15, 30, 45, 60, 75, 90, 105, 120, 135, 150
# We can see they match at 30
# So we'd have to do 30 steps before they match
# That's two loops of 15 and three loops of 10
# Now we add another number, 20
# We already know we need 30 steps to sync the first two
# So we start with 30, 60, 90, 120, 150, 180, 210, 240, 270, 300
# Then we do 20, 40, 60, 80, 100, 120, 140, 160, 180, 200
# We can see they match at 60
# So we'd have to do 60 steps before all three match
# That's why we work from the highest common number first








from collections import deque
from enum import Enum

pipes = []
with open('input.txt') as fin:
	for line in fin:
		pipes.append([n for n in line])

starting_point = None
for y in range(len(pipes)):
	for x in range(len(pipes[y])):
		if pipes[y][x] == 'S':
			starting_point = (x, y)
			break
	if starting_point:
		break

class EntryDirection(Enum):
	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3

valid_pipes = {
	EntryDirection.UP: ['|', 'J', 'L'],
	EntryDirection.DOWN: ['|', 'F', '7'],
	EntryDirection.LEFT: ['-', 'J', '7'],
	EntryDirection.RIGHT: ['-', 'F', 'L']
}
def get_adjacent_points(point) -> set[tuple]:
	x, y = point
	adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

	neighbors = set()
	for (x, y), direction in zip(adjacent, [EntryDirection.LEFT, EntryDirection.RIGHT, EntryDirection.UP, EntryDirection.DOWN]):
		if x < 0 or x >= len(pipes[0]):
			continue
		if y < 0 or y >= len(pipes):
			continue

		if pipes[y][x] in valid_pipes[direction]:
			neighbors.add((x, y))

	return neighbors

# I know Dijkstra's when I see it
# Let's see if I can implement it from scratch
# I usually do the recursive version but I think I'll try the iterative version this time
# We could do simple BFS but I just assume part 2 will add weights

nodes: dict[tuple[int,int], tuple[int, tuple[int,int]]] = {starting_point: (0, None)}
visited = {starting_point}
stack = [starting_point]
split_point = None

while stack:
	curr_point = stack.pop()
	neighbors = get_adjacent_points(curr_point)

	# # Check for a dead end
	neighbors -= visited
	if not neighbors:
		backtrack_point = curr_point
		while backtrack_point != split_point:
			backtracked = nodes.pop(backtrack_point)
			if not backtracked[1]:
				break
			backtrack_point = backtracked[1]
	# Get our split point so we know how far to backtrack
	if len(neighbors) > 1:
		split_point = curr_point

	for neighbor in neighbors:
		if neighbor in visited:
			continue
		# We don't know which nodes exist initially, so we'll add them as we go
		# Our graph is unweighted, so any adjacent node is automatically 1 away
		distance = nodes[curr_point][0] + 1
		if neighbor not in nodes or distance < nodes[neighbor][0]:
			nodes[neighbor] = (distance, curr_point)

		stack.append(neighbor)

def render_pipes():
	with open('pipes.html', 'w') as fout:
		fout.write('<style>body{font-family:monospace;} .pipe{color:red} .start{color:green}</style>')
		for y in range(len(pipes)):
			for x in range(len(pipes[y])):
				if pipes[y][x] == 'S':
					fout.write(f'<span class="start">{pipes[y][x]}</span>')
				elif (x, y) in nodes:
					fout.write(f'<span class="pipe">{pipes[y][x]}</span>')
				else:
					fout.write(pipes[y][x])
			fout.write('<br>')

render_pipes()

print(max(nodes.items(), key=lambda x: x[1][0]))






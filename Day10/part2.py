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
visited = set()
stack = [starting_point]

while stack:
	min_point = min(stack, key=lambda x: nodes[x][0])
	curr_point = stack.pop(stack.index(min_point))
	visited.add(curr_point)
	neighbors = get_adjacent_points(curr_point)
	neighbors -= visited

	# For right now, it doesn't matter which neighbor we pick cause they're all the same distance
	for neighbor in neighbors:
		distance = nodes[curr_point][0]+1

		if (neighbor not in nodes) or distance < nodes[neighbor][0]:
			nodes[neighbor] = (distance, curr_point)

	stack.extend(neighbors)

max_point = max(nodes.keys(), key=lambda x: nodes[x][0])

path_points = set()
curr_point = max_point
while True:
	path_points.add(curr_point)
	curr_point = nodes[curr_point][1]
	if curr_point is None:
		break

def render_pipes():
	with open('pipes.html', 'w') as fout:
		fout.write('<style>body{font-family:monospace;}</style>')
		for y in range(len(pipes)):
			for x in range(len(pipes[y])):
				if pipes[y][x] == 'S':
					fout.write(f'<span style="color: green">{pipes[y][x]}</span>')
				elif (x, y) == max_point:
					fout.write(f'<span style="color: green">E</span>')
				elif (x, y) in path_points:
					fout.write(f'<span style="color: blue">{pipes[y][x]}</span>')
				elif (x, y) in nodes:
					# Color based on distance
					distance = nodes[(x, y)][0]
					color = (255-distance*.02, 0, 0)
					color = ' '.join(str(int(c)) for c in color)
					fout.write(f'<span style="color:rgb({color})">{pipes[y][x]}</span>')
				else:
					fout.write(pipes[y][x])
			fout.write('<br>')

render_pipes()

print(max_point, nodes[max_point][0])






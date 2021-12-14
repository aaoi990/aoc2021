with open('day_1_input') as f:
	lines = [line.rstrip() for line in f]

lines = list(map(int, lines))

def depth_increases(v):
	return sum(b > a for a, b in zip(v, v[1:]))

windows = [sum(lines[i:i+3]) for i in range(len(lines) - 2)]

print(depth_increases(lines))
print(depth_increases(windows))

with open('day_2_input') as f:
	lines = [line.rstrip() for line in f]


def sol1(input):
	horizontal_pos = 0
	depth = 0
	for line in input:
		cmd, nums = line.split()
		if cmd == 'forward':
			horizontal_pos += int(nums)

		if cmd == 'up':
			depth -= int(nums)

		if cmd == 'down':
			depth += int(nums)

	return(horizontal_pos * depth)

def sol2(input):
	horizontal_pos, depth, aim = 0, 0, 0

	for line in input:
		cmd, nums = line.split()
		if cmd == 'forward':
			horizontal_pos += int(nums)
			depth += (aim * int(nums))

		if cmd == 'up':
			aim -= int(nums)

		if cmd == 'down':
			aim += int(nums)

	return(horizontal_pos * depth)


print(sol1(lines))
print(sol2(lines))


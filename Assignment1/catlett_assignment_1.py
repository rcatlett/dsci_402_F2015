# Ruth Catlett

def flatten(ls):
	if ls == []:
		return []
	if type(ls[0]) != type([]):
		return [ls[0]] + flatten(ls[1:])
	return flatten(ls[0]) + flatten(ls[1:])

def powerset(ls):
	if ls == []:
		return [ls]
	rest = powerset(ls[1:])
	return map(lambda x: [ls[0]] + x, rest) + powerset(ls[1:])

def all_perms(ls):
	if len(ls) <= 1:
		return [ls]	
	if len(ls) == 2:
		return [ls, ls[::-1]]

	all_p = []
	for i in range(0,len(ls)):
		rest = ls[i+1:] + ls[0:i]
		all_p += map(lambda x: [ls[i]] + x, all_perms(rest))
	return all_p
	#rest = all_perms(ls[1:])
	#return map(lambda x: [ls[0]] + x, rest) + powerset(ls[1:] + [ls[0]])

def spiral(n, end_corner = 2):
	current_position_x = 0
	current_position_y = n
	distance_to_go = n
	steps_taken = 0
	time_gone_in_direction = 1
	current_num = n**2
	directions = [(0,-1),(1,0),(0,1),(-1,0)]
	nums = []

	if end_corner == 1:
		current_position_x = -1
		current_position_y = 0
		directions = directions[1:] + [directions[0]]
	if end_corner == 3:
		current_position_x = n-1
		current_position_y = -1
		directions = directions[2:] + directions[0:2]
	if end_corner == 4:
		current_position_x = n
		current_position_y = n-1
		directions = directions[3:] + directions[0:3]
	
	for x in range(0, n):
		nums.append([])
		for y in range(0,n):
			nums[x].append(-1)

	while current_num > 0:
		current_position_x += directions[0][0]
		current_position_y += directions[0][1]
		current_num -= 1
		nums[current_position_x][current_position_y]  = current_num
		steps_taken += 1
		if steps_taken == distance_to_go:
			steps_taken = 0
			time_gone_in_direction += 1
			directions = directions[1:] + [directions[0]]
			if time_gone_in_direction == 2:
				time_gone_in_direction = 0
				distance_to_go -= 1

	for i in range(0,n):
		print nums[i]


def testing(n, t):
	if t > 0:
		print n
		next_n = (n + 2) % 4
		if next_n == 0:
			next_n = 4
		testing(next_n, t-1)
	

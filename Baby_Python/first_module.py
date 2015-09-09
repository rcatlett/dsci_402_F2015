def add_2(x, y, mult_by = 1):
	return mult_by * (x + y)
	
def optional_args_test(a, b, *rest):
	print("A: " + str(a))
	print("B: " + str(b))
	print("Rest: " + str(rest))
	
def hist(elements):
	h = {}
	for e in elements:
		if (h.has_key(e) == False):
			h[e] = 1
		else:
			h[e] = h[e] + 1
	return h					

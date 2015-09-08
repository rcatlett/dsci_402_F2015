def add_2(x, y, mult_by = 1):
	return mult_by * (x + y)
	
def optional_args_test(a, b, *rest):
	print("A: " + str(a))
	print("B: " + str(b))
	print("Rest: " + str(rest))
	
def hist(elements):
	for e in elements:
		
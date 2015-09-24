import first_module as fm

h = fm.hist([1,2,3,1,2,3])
print(h)

def greater_than(x):
	if (x > 0):
		return True
	else:
		return False

fm.my_filter(greater_than, range(-15,16))

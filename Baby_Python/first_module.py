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

def my_filter(criteria_f, elements):
	# filter out all values e in elements for
	# which criteria_f(e) == True
		
	ls = []
	
	lambda x: ls + [x] if criteria_f(x) else ls, elements
	
	return ls

def my_filter_1(criteria_f, elements):	
	return[x for x in elements if criteria_f(x)]

def my_filter_2(criteria_f, elements):
	combiner = lambda elts, elt: elts + [elt] if criteria_f(elt) else elts
	return reduce(combiner, [[]]+elements)

def sum_range(begin, end):
	return begin if begin == end else sum_range(begin, end-1) + end

def factorial(n):
	return 1 if n == 0 else factorial(n-1) * n

def rev(elements):
	return [] if elements == [] else [elements[-1]] + rev(elements[:len(elements)-1])

def hanoi(n, start, other, end):
	if n == 1:
		print("Move disk 1 from " + str(start) + " to " + str(end))
	else:
		hanoi(n - 1, start, end, other)
		print("Move disk " + str(n) + " from " + str(start) + " to " + str(end))
		hanoi(n-1, other, start, end)

#Class way
def class_fib(first, second, n):
	if n == 1:
		return first
	elif n == 2:
		return second
	return fib(first, second, n-1) + fib(first, second, n-2)
	
#My way - not good enough
def fib(first, second, n): 
	if n == 1:
		return first
	else:
		return fib(second, first+second, n-1)

#Dynamic coding
def dynamic_fib(first, second, n, cache={}):
	if n == 1:
		return first
	if n == 2:
		return second
	if not(cache.has_key(n)):
		cache[n] = dynamic_fib(first, second, n-1, cache) + dynamic_fib(first, second, n - 2, cache)
	return cache[n]

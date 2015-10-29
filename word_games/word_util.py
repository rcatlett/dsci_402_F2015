# Read in a word list in 1-word-per-line format
def read_words(filename):
	words = open(filename, 'r').readlines()
	return filter(lambda x: x != '', map(lambda y: y.strip().lower(), words))

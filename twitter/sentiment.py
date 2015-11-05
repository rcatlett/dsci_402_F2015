from twitter_util import *

# Returns a space if achar is deemed to be punctuation.
def remove_punct(char, punct):
	if char in punct:
		return ' ' 
	return char

# Reads in a file of sentiment code words and parses
# WHAT?	
def get_sentiment_codes(filename):
	lines = open(filename, 'r').readlines()
	codes = {}
	for line in lines:
		words = line.lower().strip().replace("\t", ' ').replace("\n", ' ').split(' ')
		words = filter(lambda x: x != '', words)
		code = float(words[len(words) - 1])
		codes[words[0]] = code
	return codes

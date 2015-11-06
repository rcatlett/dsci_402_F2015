from catlett_assignment_2 import *
import time

def read_words(filename):
	words = open(filename, 'r').readlines()
	return filter(lambda x: x != '', map(lambda y: y.strip().lower(), words))

words_list = read_words("../data_files/words.txt")

t0 = time.clock()
print(word_breaks("dotheredo", words_list))
w = word_breaks("something", words_list)
print(w)
t1 = time.clock() - t0
print(t1)

#print(word_breaks("applepie", words_list))

#print(word_breaks("ilikeicecreamandmango",words_list))

from word_util import *
from anagram import *
import time

words = read_words("../data_files/words.txt")

t0 = time.clock()
print(anagram("listen", words))
t1 = time.clock() 
print(t1-t0)

t0 = time.clock()
s = list("listen")
s.sort()
anagrams = []
for w in words:
	wh = list(w)
	wh.sort()
	if wh == s:
		anagrams.append(w)
print(anagrams) 
print(time.clock() - t0)

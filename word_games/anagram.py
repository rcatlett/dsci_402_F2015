# Build a word histogram
def word_hist(word):
	h = {}
	for let in word:
		if not h.has_key(let):
			h[let] = 0
		h[let] += 1
	return h

def anagram(word, word_list):
	wh = word_hist(word)
	anagrams = []
	for w in word_list:
		if word_hist(w) == wh:
			anagrams.append(w)
	return anagrams				

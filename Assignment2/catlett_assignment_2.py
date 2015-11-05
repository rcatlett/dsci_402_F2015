def word_breaks(word, word_list):
	parts = []

	for i in range(1,len(word)+1):
		p = []
		w = word[0:i]
		if w in word_list:
			parts.append(w)
			parts+= [word_breaks(word[i:], word_list)]
	return parts


"""
dotheredo

d - not a word
do - this is a word!! theredo?
dot - a word! heredo?
doth - a word! eredo?
dothe - not a word
dother - not a word
dothere - not a word
dothered - not a word
dotheredo - the word, not a word
"""

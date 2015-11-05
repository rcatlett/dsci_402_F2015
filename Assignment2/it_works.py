def word_breaks(word, word_list):
	parts = []

	for i in range(len(word)+1):
		p = []
		w = word[0:i]
		if w in word_list:
			p.append(w)
			trial = word_breaks(word[i:], word_list)			
			for t in trial:
				total_now = ''.join(p)
				total_trial = ''.join(t)
				if total_now+total_trial == word:
					p += t
					parts.append(p)
			if ''.join(p) == word:
				parts.append(p)
	return parts

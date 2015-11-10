def word_breaks(word, word_list):
	parts = []
	
	for i in range(len(word)+1):
		w = word[0:i]
		if w in word_list:
			if w == word:
				parts.append([w])
			else:
				wb = word_breaks(word[i:], word_list)			
				for n in wb:
					next_part = ''
					for word_part in n:
						next_part += word_part
					if w+next_part == word:
						parts.append([w]+n)					
	while '' in parts:
		parts.remove('')
	return parts

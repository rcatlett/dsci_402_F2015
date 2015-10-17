all_words = read_words('words.txt')
perms = all_perms(word)
anagrams = []

for perm in perms:
	for word in words:
		if perm == word:
			anagrams.apend(word)
return anagrams

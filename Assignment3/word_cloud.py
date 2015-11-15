from sentiment import *
from twitter_util import *

def infer_word_sentiments(codes, text):
	inferred = {}
	score = 0
	for t in text:
		score = sentiment_score(codes, t)
		clean_text = ''.join(map(lambda x: remove_punct(x, standard_punct_list()), t)).lower()
		words = filter(lambda x: x != '', clean_text.split(' '))
		for w in words:
			if not(w in codes):
				if not(inferred.has_key(w)):
					inferred[w] = (0, 0)
				inferred[w] = tuple(map(lambda x, y: x + y, inferred[w], (score, 1)))				
	for word in inferred:
		s, wc = inferred[word]
		inferred[word] = float(s) / float(wc)		
		
	return inferred	

def infer_tweet_word_sentiments(codes, tweets):
	texts = []
	for tweet in tweets:
		texts.append(text(tweet))
	return infer_word_sentiments(codes, texts)

def top_n_words(sentiment_score_dict, n, direction = 1):
	srt = sorted(sentiment_score_dict.items(), key = lambda x: x[1])
	
	if direction == 1:
		srt.reverse()
	
	top = []
	for i in range(n):
		top.append(srt[i])
	return top

def build_word_cloud_list(sentiment_score_dict, n, filename, direction = 1):
	words = top_n_words(sentiment_score_dict, n, direction)
	f = open(filename, 'w')

	top = words[0][1]

	for word in words:
		times = int(word[1] * 10 / top)
		for i in range(times):
			f.write(word[0])
			f.write("\n")
	f.close()					

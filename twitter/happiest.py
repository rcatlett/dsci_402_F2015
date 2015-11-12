from twitter_util import *
from sentiment import *

def get_states(file):
	states = {}
	words = open(file, 'r').readlines()
	for line in words:
		line = line.replace("\n", "")
		part = line.split(",")
		states[part[0]] = part[1]
		states[part[1]] = part[1]
	return states

def get_state(tweet):
	# Get location off tweet
	return text(tweet, ['user', 'location'])

def rank_tweets(tweet_file, n):
	states = get_states("../data_files/states.txt")
	codes = get_sentiment_codes("AFINN-111.txt")
	scores = {}
	tweets = read_tweets(tweet_file)
	for t in tweets:
		state = get_state(t)
		txt = text(t, 'text')
		for key in states:
			if key in state:
				# Only catches exact matches (eg. 'oregon' doesnt catch)
				state = states[key]
				if not(scores.has_key(state)):
					scores[state] = (0,0)
			
				my_score = sentiment_score(codes, txt)
				scores[state] = tuple(map(lambda x, y: x + y, scores[state], (my_score, 1)))
	# Normalize
	for s in scores:
		scores[s] = scores[s][0] / scores[s][1]

	# Order by Value
	srt = sorted(scores.items(),key = lambda x : x[1])
	
	# print first n
	print("Unhappiest")
	for i in range(n):
		print(srt[i])
		print("\n")
	
	srt.reverse()
	print("Happiest")
	for i in range(n):
		print(srt[i])
		print("\n")

print("---- Hillary ----")
rank_tweets("./twitter_data/hillary.json", 5)

print("---- Trump ----")
rank_tweets("./twitter_data/trump.json", 5)
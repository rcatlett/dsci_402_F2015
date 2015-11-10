def get_states(file):
	states = {}
	for line in file:
		part = line.split(",")
		states[part[1]] = part[0]
		states[part[1]] = part[1]
	return states

def get_state(tweet):
	# Get location off tweet

def rank_tweets(tweets):
	states = get_states("../data_files/states.txt")
	
	for t in tweets:
		states = get_state(tweet)
		cs, cwc = states[state]
		states[state] = (cs + sentiment(t), (wc + wc(t)))
	
	# Normalize
	# Order by Value
	# print first n
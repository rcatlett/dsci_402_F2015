from twitter_util import *
from sentiment import *

#texts = read_texts("twitter_data/adele.json")

#print(texts)

codes = get_sentiment_codes("AFINN-111.txt")
#print(codes)

trump = read_texts("twitter_data/trump.json")
hillary = read_texts("twitter_data/hillary.json")

print("Trump\n")
for t in trump[:10]:
	print(t, sentiment_score(codes, t))

print("Hillary\n")
for h in hillary[:10]:
	print(h, sentiment_score(codes, h))
	
print("Adele\n")
adele = read_tweets("twitter_data/adele.json")
for a in adele[:10]:
	print(text(t, ['user', 'location']))

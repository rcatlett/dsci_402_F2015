from twitter_util import *
from sentiment import *
from word_cloud import *

codes = get_sentiment_codes("AFINN-111.txt")

trump = read_tweets("twitter_data/trump.json")
hillary = read_tweets("twitter_data/hillary.json")
adele = read_tweets("twitter_data/adele.json")

print("Trump\n")
infer = infer_tweet_word_sentiments(codes, trump)
build_word_cloud_list(infer, 10, "trump.txt", 1)

print("Hillary\n")
infer = infer_tweet_word_sentiments(codes, hillary)
build_word_cloud_list(infer, 10, "hillary.txt", 1)

print("Adele\n")
infer = infer_tweet_word_sentiments(codes, adele)
build_word_cloud_list(infer, 10, "adele.txt", 1)

now = read_tweets("sample_now.json")
infer = infer_tweet_word_sentiments(codes, now)
print(infer)
build_word_cloud_list(infer, 10, "now.txt", 1)

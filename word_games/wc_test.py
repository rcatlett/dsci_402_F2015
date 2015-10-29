from word_chains import *
from word_util import *

print(one_off("beet", "beat"))
print(one_off("beet", "beet"))
print(one_off("boom", "books"))
print(one_off("beam", "book"))

# Assumes words from wor director
words = read_words('../data_files/words.txt')
graph = build_graph(words, 4)
print(graph["beat"])
print(word_chain(graph, "bear", "beef", 4))

graph = build_graph(words, 6)
print(word_chain(graph, "charge", "comedo", 50))

from catlett_assignment_2 import *
import time

words_list = read_words("../data_files/words.txt")

t0 = time.clock()
word_breaks("something", words_list)
t1 = time.clock() - t0
print(t1-t0)

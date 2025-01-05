import sys
import math
import string
import csv
from collections import defaultdict
from glob import glob
from get_durations import get_csv_lines, get_durations
from get_surprisals import get_lines, get_unigrams, get_bigrams, get_surprisal, get_bigram_surprisal, get_test_surprisal
import pandas as pd

def main():

    # get train data
    filename = sys.argv[1]
    train_sentences = get_lines(filename)
    train_unigram = get_unigrams(train_sentences)
    train_bigram = get_bigrams(train_sentences)
    train_bigram_surprisal = get_bigram_surprisal(train_unigram,train_bigram)

    # get test data
    data = []
    testfiles = glob(f"{sys.argv[2]}/*")
    for testfile in testfiles:
        test_sentence = get_csv_lines(testfile)
        duration_dict = get_durations(test_sentence)
        # print(duration_dict)
        test_word_surprisal = get_test_surprisal(duration_dict, train_bigram_surprisal)
        # print(test_word_surprisal)

    # build an empty list, store word, durating, surprisal
        for key, duration in duration_dict.items():
            word = key[1]
            if word in test_word_surprisal:
                surprisal = test_word_surprisal[word]
                data.append([word, duration, surprisal])
    '''print(data) At this point, all words in each sentence (including the same words) 
    and their duration and surprisal will be added into data list.'''

    # convert data list into a pandas DataFrame
    df = pd.DataFrame(data, columns=['word', 'duration', 'surprisal'])
    averages = df.groupby('word', as_index=False).mean()
    averages.to_csv('Data.csv', index=False)
main()
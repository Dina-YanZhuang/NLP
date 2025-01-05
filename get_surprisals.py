import math
import string
from collections import defaultdict
from nltk import sent_tokenize, word_tokenize

def get_lines(filename):
    with open(filename, mode ="r", encoding = "utf-8") as f:
        lines = f.read()
    sentences = sent_tokenize(lines)
    return sentences

def get_unigrams(sentences):
    unigram = defaultdict(int)
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word for word in words if word not in string.punctuation]
        for word in words:
            unigram[word.lower()] += 1
    return unigram

def get_bigrams(sentences):
    bigram = defaultdict(int)
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word for word in words if word not in string.punctuation]
        for w1, w2 in zip(words, words[1:]):
            bigram[(w1.lower(), w2.lower())] += 1
    return bigram

def get_surprisal(prob):
    return -math.log2(prob)

def get_bigram_surprisal(unigram, bigram):
    bigram_surprisal = defaultdict(float)
    for key in bigram.keys():
        first_word = key[0]    
        prob_first_word = unigram.get(first_word,0)
        bigram_freq = bigram.get(key,0)
        bigram_prob = bigram_freq / prob_first_word
        surprisal = get_surprisal(bigram_prob)
        bigram_surprisal[key] = surprisal
    return bigram_surprisal

def get_test_surprisal(duration_dict, train_bigram_surprisal):
    test_word_surprisal = defaultdict(float)
    for key in duration_dict.keys():
        word = key[1]
        total_surprisal = 0.0
        count = 0
        for key, value in train_bigram_surprisal.items():
            if key[1] == word:
                total_surprisal += value
                count += 1
        if count > 0:
            average_surprisal = total_surprisal / count
            test_word_surprisal[word] = average_surprisal
    return test_word_surprisal

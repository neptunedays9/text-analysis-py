
from nltk import FreqDist

#librraies for visualisation


def freq_words(text_array):
    fdist = FreqDist(text_array)
    return fdist

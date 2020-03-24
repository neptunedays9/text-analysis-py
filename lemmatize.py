from nltk.stem.wordnet import WordNetLemmatizer


def lemmatize(text_array):
    text_array_new = []
    for t in text_array:
        text_array_new.append(WordNetLemmatizer().lemmatize(t, 'v'))

    return text_array_new
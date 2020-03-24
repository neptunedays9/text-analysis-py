from nltk.corpus import stopwords
stop_words = stopwords.words('english')

#to remove stopwords


def remove_stopwords(rev):
    rev_new = " ".join([i for i in rev if i not in stop_words])
    return rev_new
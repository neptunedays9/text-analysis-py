import pandas as pd
import numpy as np
import re
import spacy

import matplotlib.pyplot as plt
import seaborn as sns

def show_data(fdist, terms = 30):
    words_df = pd.DataFrame({'word': list(fdist.keys()), 'count': list(fdist.values)})

    #selecting top20 most frequent words
    d = words_df.nlargest(columns="count", n = terms)
    plt.figure(figsize=(20,5))
    ax = sns.barplot(data=d, x="word", y="count")
    ax.set(ylabel = 'count')
    plt.show()
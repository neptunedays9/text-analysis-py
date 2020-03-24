import spacy
from sklearn.decomposition import LatenDirichletAllocation

import pandas as pd

import numpy as np

from sklearn.model_selection import GridSearchCV

nlp = spacy.load('en', disable=['parser', 'ner'])


def predict_topic(lda_model, text, nlp=nlp):
    global sent_to_words
    global lemmatization

    # define search param
    search_params = {'n_components': [10, 15, 20, 25, 30], 'learning_decay': [0.5, 0.7, 0.9]}

    #init the model
    lda = LatenDirichletAllocation()

    model = GridSearchCV(lda, param_grid=search_params)

    topic_probability_scores = lda_model.transform(text)

    df_topic_keywords = pd.DataFrame(lda_model.components_)

    topic = df_topic_keywords.iloc[np.argmax(topic_probability_scores, :].values.tolist()
    return topic, topic_probability_scores
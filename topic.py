from pprint import pprint

import gensim
from gensim import corpora

#librraies for visualisation
import pyLDAvis
import pyLDAvis.gensim

from topic_wordcloud import show_topic_wordcloud

lda_model = Nonedoc_term_matrix = None

dictionary = None
def build_topic_model_dict(text_array):
    global dictionary
    dictionary = corpora.Dictionary(text_array)

    global doc_term_matrix
    doc_term_matrix = [dictionary.doc2bow(rev) for rev in text_array]

    #creating the object for LDA model using gensim library
    LDA = gensim.models.ldamodel.LdaModel

    #build the model
    global lda_model
    lda_model = LDA(corpus=doc_term_matrix, id2word=dictionary, num_topics=7,
                    random_state=100, chunksize=1000, passes=50)

    #print topics
    #lda_model.print_topics()

    pyLDAvis.enable_notebook()

def show_lda_html():
    global lda_model, doc_term_matrix, dictionary
    vis = pyLDAvis.gensim.prepate(lda_model, doc_term_matrix, dictionary)
    #print(vis)
    pyLDAvis.save_html(vis, 'LDA_visualisation.html')
    #vis

def show_wordcloud():
    global lda_model
    show_topic_wordcloud(lda_model)

def show_lda_topics():
    #print(lda_model)
    pprint(lda_model.print_topics())

def predict(text):
    global lda_model
    bow = dictionary.doc2bow(text.split())
    print(lda_model.get_document_topics(bow,minimum_probability=0.0))

    #topic,prob_scores = predict_topics(lda_model,text)
    #print(topic)
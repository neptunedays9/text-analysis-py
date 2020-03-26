from frequency import freq_words

from stopwords import remove_stopwords

from data import read_raw_data, \
    write_data_token_frequency, \
    read_dict_token, \
    read_dict_textarray, \
    write_data_text_array

from display import show_data

from topic import build_topic_model_dict, show_lda_html, show_wordcloud, predict, show_lda_topics

from character_filter import remove_unwanted_characters

from lemmatize import lemmatize

from postag import token_postag

token_dict = {}

text_array = []


def process_text():
    # text = "the phone camera is awesome"

    collection = read_raw_data()

    for record in collection.find({}):

        text = record['text']
        text = text.lower()
        tmp_text_array = text.split(" ")

        tmp_text_array = remove_unwanted_characters(tmp_text_array)

        # Change caring to care
        tmp_text_array = lemmatize(tmp_text_array)

        # remove and be mine
        tmp_text_array = remove_stopwords(tmp_text_array)

        tmp_text_array = token_postag(tmp_text_array)

        text_array.append(tmp_text_array)

        dict = freq_words(tmp_text_array)

        write_data_text_array(text_array)

        text_array.clear()

        write_data_token_frequency(dict)


def read_token_dict():
    text_collection = read_dict_token()
    for record in text_collection.find({}):
        token_dict.update({record['token']: record['count']})


def read_text_array():
    text_collection = read_dict_textarray()
    for record in text_collection.find({}):
        text_array.append(record['textarray'])


def show_frequency_graph():
    show_data(token_dict)


def build_topic_model():
    print(text_array)
    build_topic_model_dict(text_array)


def show_topics_wordcloud():
    show_wordcloud()


def show_topics_lda_html():
    show_lda_html()


def predict_topic():
    # predict the text
    mytext = "phone model"
    predict(mytext)


def show_topics_lda():
    show_lda_topics()

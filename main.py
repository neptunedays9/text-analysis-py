# nltk.download('stopwords') #run this line onetime

from process import \
    process_text, \
    show_frequency_graph, \
    build_topic_model, \
    read_token_dict, \
    read_text_array, \
    show_topics_wordcloud, \
    show_topics_lda, \
    show_topics_lda_html, \
    predict_topic

# once - creates tokens and writes to total count per token in DB
process_text()

# read from token, count from DB and create a dictionary
read_token_dict()

# read the array of tojens per sentense
read_text_array()

# build the model
build_topic_model()
print("model build complete")

# for display

show_frequency_graph()

show_topics_lda_html()

show_topics_wordcloud()

# predict
# predict_topic()

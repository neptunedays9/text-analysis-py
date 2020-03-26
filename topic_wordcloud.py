# 1. Wordcloud of top N words in each topic

from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import matplotlib.colors as mcolors

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

cols = [color for name, color in mcolors.TABLEAU_COLOURS.items()]


def show_topic_wordcloud(lda_model):
    topics = lda_model.show_topics(formatted=False)

    fig, axes = plt.subplots(2, 2, figsize=(10, 10), sharex=True, sharey=True)

    for i, ax in enumerate(axes.flatten()):
        cloud = WordCloud(stopwords=stop_words,
                          background_color='white',
                          width=2500,
                          height=1800,
                          max_words=10,
                          colormap='tab10',
                          color_func=lambda *args, **kwargs: cols[i],
                          prefer_horizontal=1.0)
        
        fig.add_subplot(ax)
        topic_words = dict(topics[i][1])
        cloud.generate_from_frequencies(topic_words, max_font_size=300)
        plt.gca().imshow(cloud)
        plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
        plt.gca().axis('off')

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.axis('off')
    plt.margin(x=0, y=0)
    plt.tight_layout()
    plt.show()
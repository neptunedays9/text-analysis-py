import nltk


def token_postag(text):
    text_array = []
    tokens = nltk.word_tokenizer(text)
    for tuple in nltk.pos_tag(tokens):
        if tuple[1] == "NN" or tuple[1] == "JJ":
            text_array.append(tuple[0])
    return text_array

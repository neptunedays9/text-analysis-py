import re


def remove_unwanted_characters(text_array):
    # print(text_array)
    text_array_new = []

    for t in text_array:
        if len(t) > 1:
            t = re.sub('[^A-Za-z0-9]+', '', t)
            text_array_new.append(t)

    return text_array_new
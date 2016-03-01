import os

from textblob import TextBlob


# read in list of word
def clean_data_(data):
    # filter with stop words
    fn = os.path.join(os.path.dirname(__file__), 'stop_words_en.txt')
    stop_word_list = open(fn, 'rb').read().split()

    new_data = []
    for word in data:
        if word not in stop_word_list:
            new_data.append(word)

    singular_data = []
    # get rid of singular and plural forms
    sentence = TextBlob(' '.join(data))
    for i in range(len(sentence.words) - 1):
        singular_data.append(sentence.words[i].singularize())

    return singular_data

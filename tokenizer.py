from nltk.tokenize import word_tokenize

def create_word_features(words):
    my_dict = dict( [ (word, True) for word in words] )
    return my_dict
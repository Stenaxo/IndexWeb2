from nltk.stem.porter import PorterStemmer

def stem_tokens(tokens):

    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens
import nltk
import string


stopwords = nltk.corpus.stopwords.words('norwegian')


def bi_tri_stopwords(tokens):
    lowered = [token.lower() for token in tokens if token not in stopwords and token not in string.punctuation]
    tokens_cleaned = [bigram for bigram in nltk.bigrams(lowered)]
    for token in lowered:
        tokens_cleaned.append((token,))

    for trigram in nltk.trigrams(lowered):
        tokens_cleaned.append(trigram)

    tokens_dict = dict([token, True] for token in tokens_cleaned)
    return tokens_dict


def bigrams_stopwords(tokens):
    lowered = [token.lower() for token in tokens if token not in stopwords and token not in string.punctuation]
    tokens_cleaned = [bigram for bigram in nltk.bigrams(lowered)]
    for token in lowered:
        tokens_cleaned.append((token,))

    tokens_dict = dict([token, True] for token in tokens_cleaned)
    return tokens_dict


def bigrams(tokens):
    lowered = [token.lower() for token in tokens if token not in string.punctuation]
    tokens_cleaned = [bigram for bigram in nltk.bigrams(lowered)]
    for token in lowered:
        tokens_cleaned.append((token,))

    tokens_dict = dict([token, True] for token in tokens_cleaned)
    return tokens_dict

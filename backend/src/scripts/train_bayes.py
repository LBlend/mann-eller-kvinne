import nltk
import pickle
import itertools
from string import punctuation

stopwords = nltk.corpus.stopwords.words('norwegian')

def preprocess(tokens, trigrams=False, use_stopwords=False):
    normalized = (token.lower() for token in tokens if token not in punctuation)

    if not use_stopwords:
        normalized = filter(lambda x: x not in stopwords, normalized)

    lowered = list(normalized)
    # Make iterator over all elements
    token_iter = itertools.chain(((w,) for w in lowered),
                               nltk.bigrams(lowered),
                               nltk.trigrams(lowered) if trigrams else []
                               )

    return {token: True for token in token_iter}


def load_corpus():
    return nltk.corpus.PlaintextCorpusReader('corpus/data/train', r'.*\.txt')


def get_text(text):
    man, woman = [], []
    for file in text.fileids():
        if file.startswith('M'):
            man.append([word.lower() for word in text.words(file)])
        elif file.startswith('F'):
            woman.append([word.lower() for word in text.words(file)])
    return man, woman


def save_model(model, path):
    with open(path, 'wb') as f:
        pickle.dump(model, f)


def train(path):
    corpus = load_corpus()
    man, woman = get_text(corpus)

    man_feat = [(preprocess(words), 'man') for words in man]
    woman_feat = [(preprocess(words), 'woman') for words in woman]

    train_set = man_feat + woman_feat
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    # Function below outputs to terminal
    classifier.show_most_informative_features(10)

    save_model(classifier, path)

    return classifier

if __name__ == '__main__':
    train('bin/bayes_model.pkl')

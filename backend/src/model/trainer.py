import nltk
import feature_extractor

import pickle


def load_corpus():
    return nltk.corpus.PlaintextCorpusReader('corpus/NoRec_gender/', r'.*\.txt')


def get_text(text, man, woman):
    for file in text.fileids():
        if file.startswith('M'):
            man.append([word.lower() for word in text.words(file)])
        elif file.startswith('F'):
            woman.append([word.lower() for word in text.words(file)])
    return man, woman


def save_model(model):
    with open('model.pickle', 'wb') as f:
        pickle.dump(model, f)


def main():
    man = []
    woman = []

    text = load_corpus()
    man_feat, woman_feat = get_text(text, man, woman)

    man_feat = []
    for words in man:
        man_feat.append((feature_extractor.bigrams_stopwords(words), 'man'))

    woman_feat = []
    for words in woman:
        woman_feat.append((feature_extractor.bigrams_stopwords(words), 'woman'))

    train_set = man_feat + woman_feat
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(classifier.show_most_informative_features(10))

    save_model(classifier)


if __name__ == '__main__':
    main()

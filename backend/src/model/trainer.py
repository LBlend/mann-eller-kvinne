import nltk
import feature_extractor

import pickle


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


def save_model(model):
    with open('src/model/bayes_model.pkl', 'wb') as f:
        pickle.dump(model, f)


def main():
    text = load_corpus()
    man, woman = get_text(text)

    man_feat = [(feature_extractor.bigrams_stopwords(words), 'man') for words in man]
    woman_feat = [(feature_extractor.bigrams_stopwords(words), 'woman') for words in woman]

    train_set = man_feat + woman_feat
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    # Function below outputs to terminal
    classifier.show_most_informative_features(10)

    save_model(classifier)


if __name__ == '__main__':
    main()

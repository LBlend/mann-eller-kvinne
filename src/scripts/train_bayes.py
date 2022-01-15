import itertools
import nltk
import pickle
from string import punctuation


STOPWORDS = nltk.corpus.stopwords.words("norwegian")


def preprocess(
    tokens: list[str], trigrams: bool = False, use_stopwords: bool = False
) -> dict[str, bool | None]:
    normalized = (token.lower() for token in tokens if token not in punctuation)

    if not use_stopwords:
        normalized = filter(lambda x: x not in STOPWORDS, normalized)

    lowered = list(normalized)
    # Make iterator over all elements
    token_iter = itertools.chain(
        ((w,) for w in lowered),
        nltk.bigrams(lowered),
        nltk.trigrams(lowered) if trigrams else [],
    )

    return {token: True for token in token_iter}


def _load_corpus() -> nltk.corpus.PlaintextCorpusReader:
    return nltk.corpus.PlaintextCorpusReader("corpus/data/train", r".*\.txt")


def get_text(text: str) -> tuple[list[list[str]], list[list[str]]]:
    man, woman = [], []

    for file in text.fileids():
        if file.startswith("M"):
            man.append([word.lower() for word in text.words(file)])
        elif file.startswith("F"):
            woman.append([word.lower() for word in text.words(file)])

    return man, woman


def _save_model(model, path: str) -> None:
    with open(path, "wb") as f:
        pickle.dump(model, f)


def train(path: str) -> nltk.NaiveBayesClassifier:
    corpus = _load_corpus()
    man, woman = get_text(corpus)

    man_feat = [(preprocess(words), "man") for words in man]
    woman_feat = [(preprocess(words), "woman") for words in woman]

    train_set = man_feat + woman_feat
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    classifier.show_most_informative_features(10)  # Function below outputs to terminal

    _save_model(classifier, path)

    return classifier


if __name__ == "__main__":
    train("src/bin/bayes_model.pkl")

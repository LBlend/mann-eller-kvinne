import nltk
import pickle
from string import punctuation
from numpy import vectorize
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import os
import numpy as np

MODEL_PATH = "src/bin/bayes_model_sk.pkl"
VECTORIZER_PATH = "src/bin/vectorizer.pkl"

STOPWORDS = nltk.corpus.stopwords.words("norwegian")
np.random.seed(42)


def read_file(path: str) -> str:
    with open(path) as f:
        content = f.read()
    return content


def _load_corpus() -> tuple[list[str] | np.ndarray]:
    dir_f = "corpus/data/train/F/"
    dir_m = "corpus/data/train/M/"
    files_f = [dir_f + i for i in os.listdir(dir_f)]
    files_m = [dir_m + i for i in os.listdir(dir_m)]
    labels_f = np.full(len(files_f), "F")
    labels_m = np.full(len(files_m), "M")

    raw_data = list(map(read_file, files_f + files_m))
    labels = np.concatenate((labels_f, labels_m))
    return raw_data, labels


def _save_model(model: MultinomialNB, path: str) -> None:
    with open(path, "wb+") as f:
        pickle.dump(model, f)


def train() -> None:
    raw_data, labels = _load_corpus()

    vectorizer = CountVectorizer(
        stop_words=STOPWORDS,
        ngram_range=[1, 3],  # for usage of trigrams and bigrams
        max_features=5000,
    )

    features = vectorizer.fit_transform(raw_data)
    # shuffle data in case it is not permutation invariant
    perms = np.random.permutation(len(labels))
    # Does CSRMatrix handle this?
    features = features[perms]
    labels = labels[perms]

    clf = MultinomialNB(fit_prior=False)

    clf.fit(features, labels)

    _save_model(clf, MODEL_PATH)
    _save_model(vectorizer, VECTORIZER_PATH)


if __name__ == "__main__":
    train()

import nltk
from model import feature_extractor
import pickle


with open('./model/model.pickle', 'rb') as f:
    classifier = pickle.load(f)


def predict(text):
    result = {}

    text_tokens = nltk.tokenize.word_tokenize(text)
    text_features = feature_extractor.bigrams_stopwords(text_tokens)
    prediction = classifier.prob_classify(text_features)

    result['text'] = text
    result['prediction'] = prediction.max()
    result['likelyhood'] = {}
    result['likelyhood']['raw'] = {}
    result['likelyhood']['simple'] = {}

    result['likelyhood']['raw']['man'] = prediction.prob('man')
    result['likelyhood']['raw']['woman'] = prediction.prob('woman')

    result['likelyhood']['simple']['man'] = f'{prediction.prob("man") * 100:.2f}%'
    result['likelyhood']['simple']['woman'] = f'{prediction.prob("woman") * 100:.2f}%'

    return result

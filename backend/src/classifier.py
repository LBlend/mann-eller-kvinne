import nltk
from model import feature_extractor
import pickle


with open('./model/bayes_model.pkl', 'rb') as f:
    classifier = pickle.load(f)


def predict(text):
    result = {}

    text_tokens = nltk.tokenize.word_tokenize(text)
    text_features = feature_extractor.bigrams_stopwords(text_tokens)
    prediction = classifier.prob_classify(text_features)

    norwegian = {
        'man': 'mann',
        'woman': 'kvinne'
    }

    result = {
        'text': text,
        'prediction': {
            'norwegian': norwegian[prediction.max()],
            'english': prediction.max()
        },
        'likelihood': {
            'raw': {
                'man': prediction.prob('man'),
                'woman': prediction.prob('woman')
            },
            'simple': {
                'man': f'{prediction.prob("man") * 100:.0f}%',
                'woman': f'{prediction.prob("woman") * 100:.0f}%'
            }
        }
    }

    return result

import numpy as np
import nltk
import pickle
import os
from scripts import train_bayes
# SUPPRESS WARNINGS
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow import keras  # noqa: E402


with open('bin/bayes_model.pkl', 'rb') as f:
    bayes_model = pickle.load(f)

rnn_model = keras.models.load_model('bin/rnn')


def predict_bayes(text):
    text_tokens = nltk.tokenize.word_tokenize(text)
    text_features = train_bayes.preprocess(text_tokens)
    dist = bayes_model.prob_classify(text_features)
    return {'M': dist.prob('man'), 'F': dist.prob('woman')}


def predict_rnn(text):
    pred_arr = rnn_model.predict(np.array([text]))
    pred = float(pred_arr[0, 0])
    # F = 0, M = 1, P(!A) == 1 - P(A)
    return {'M': pred, 'F': 1 - pred}


pred_funcs = {
    'bayes': predict_bayes,
    'rnn': predict_rnn
}


def predict(text, clf='bayes'):
    predict_proba = pred_funcs[clf]
    return {
        'text': text,
        'clf': clf,
        'probability': predict_proba(text)
    }

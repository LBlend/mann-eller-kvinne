import numpy as np
import pickle
import os

# SUPPRESS WARNINGS
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
from tensorflow import keras  # noqa: E402


with open("src/bin/bayes_model_sk.pkl", "rb") as f:
    bayes_model = pickle.load(f)

with open("src/bin/logreg_model_sk.pkl", "rb") as f:
    logreg_model = pickle.load(f)

with open("src/bin/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

rnn_model = keras.models.load_model("src/bin/rnn")


def predict_bayes(text: str) -> dict[str, float]:
    features = vectorizer.transform([text])
    probs = bayes_model.predict_proba(features)[0]
    return {
        "male": probs[1],
        "female": probs[0],
    }


def predict_logreg(text: str) -> dict[str, float]:
    features = vectorizer.transform([text])
    probs = logreg_model.predict_proba(features)[0]
    return {
        "male": probs[1],
        "female": probs[0],
    }


def predict_rnn(text: str) -> dict[str, float]:
    pred_arr = rnn_model.predict(np.array([text]))
    pred = float(pred_arr[0, 0])
    # F = 0, M = 1, P(!A) == 1 - P(A)
    return {"male": pred, "female": 1 - pred}


pred_funcs = {"bayes": predict_bayes, "rnn": predict_rnn, "logreg": predict_logreg}


def predict(text: str, classifier: str = "bayes") -> dict[str, str | dict[str, float]]:
    predict_proba = pred_funcs[classifier]
    return {"text": text, "classifier": classifier, "probability": predict_proba(text)}

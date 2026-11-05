import os
import pickle
import warnings
from pathlib import Path

# SUPPRESS WARNINGS
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
warnings.filterwarnings('ignore')

import tensorflow as tf  # noqa: E402
from tensorflow import keras  # noqa: E402

BIN_DIR = Path(__file__).parent / "bin"


def _load_pickle(path: Path):
    if path.stat().st_mode & 0o002:
        raise PermissionError(f"Refusing to load world-writable file: {path}")

    with path.open("rb") as f:
        return pickle.load(f)


bayes_model = _load_pickle(BIN_DIR / "bayes_model_sk.pkl")
vectorizer = _load_pickle(BIN_DIR / "vectorizer.pkl")
rnn_model = keras.models.load_model(BIN_DIR / "rnn.keras", safe_mode=True)


def predict_bayes(text: str) -> dict[str, float]:
    features = vectorizer.transform([text])
    probs = dict(zip(bayes_model.classes_, bayes_model.predict_proba(features)[0]))
    return {"male": float(probs["M"]), "female": float(probs["F"])}


def predict_rnn(text: str) -> dict[str, float]:
    pred = float(rnn_model(tf.constant([text]), training=False)[0, 0])
    # F = 0, M = 1, P(!A) == 1 - P(A)
    return {"male": pred, "female": 1 - pred}


pred_funcs = {"bayes": predict_bayes, "rnn": predict_rnn}


def predict(text: str, classifier: str = "bayes") -> dict[str, str | dict[str, float]]:
    if classifier not in pred_funcs:
        raise ValueError(f"Unknown classifier: {classifier}. Must be one of {list(pred_funcs)}")

    return {"text": text, "classifier": classifier, "probability": pred_funcs[classifier](text)}

import pickle
import os
import warnings
from pathlib import Path

# SUPPRESS WARNINGS
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
warnings.filterwarnings('ignore')

import tensorflow as tf  # noqa: E402
from tensorflow import keras  # noqa: E402

BIN_DIR = Path(__file__).parent / "bin"

# Security note: Pickle files can execute arbitrary code when loaded.
# These files should only be loaded from trusted sources and protected with
# appropriate file permissions. In production, consider using safer serialization
# formats like joblib or JSON + model-specific loaders.


def safe_pickle_load(filepath: str):
    """
    Load pickle file with basic safety checks.
    WARNING: This is not completely secure against malicious pickle files.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Model file not found: {filepath}")

    # Check file permissions (should not be world-writable)
    file_stat = os.stat(filepath)
    if file_stat.st_mode & 0o002:  # Check if world-writable
        raise PermissionError(f"Unsafe permissions on {filepath}")

    with open(filepath, "rb") as f:
        return pickle.load(f)


# Load models with safety checks
try:
    bayes_model = safe_pickle_load(BIN_DIR / "bayes_model_sk.pkl")
    vectorizer = safe_pickle_load(BIN_DIR / "vectorizer.pkl")

    rnn_model = keras.models.load_model(BIN_DIR / "rnn.keras", safe_mode=True)
except Exception as e:
    print(f"Error loading models: {e}")
    raise


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
        raise ValueError(f"Unknown classifier: {classifier}. Must be one of {list(pred_funcs.keys())}")

    predict_proba = pred_funcs[classifier]
    return {"text": text, "classifier": classifier, "probability": predict_proba(text)}

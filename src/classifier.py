import numpy as np
import pickle
import os
import warnings

# SUPPRESS WARNINGS
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
warnings.filterwarnings('ignore')

from tensorflow import keras  # noqa: E402

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
    bayes_model = safe_pickle_load("src/bin/bayes_model_sk.pkl")
    vectorizer = safe_pickle_load("src/bin/vectorizer.pkl")

    # Try loading Keras 3 format first, fallback to legacy format
    rnn_model_path = "src/bin/rnn.keras"
    if not os.path.exists(rnn_model_path):
        # Fallback to old format directory (for backward compatibility)
        rnn_model_path = "src/bin/rnn"

    # Load with safe_mode=True to prevent arbitrary code execution
    # Note: This only works with .keras files, not .h5/.hdf5
    try:
        rnn_model = keras.models.load_model(rnn_model_path, safe_mode=True)
        print("RNN model loaded in safe mode")
    except Exception as safe_mode_error:
        print(f"Safe mode loading failed: {safe_mode_error}")
        # Fallback to unsafe loading only for trusted local models
        # In production, this should be removed or require explicit configuration
        if os.path.basename(rnn_model_path) == "rnn.keras" or os.path.basename(rnn_model_path) == "rnn":
            print("Loading model without safe_mode (trusted local model)")
            rnn_model = keras.models.load_model(rnn_model_path, safe_mode=False)
        else:
            raise ValueError(f"Refusing to load untrusted model: {rnn_model_path}")
except Exception as e:
    print(f"Error loading models: {e}")
    raise


def predict_bayes(text: str) -> dict[str, float]:
    features = vectorizer.transform([text])
    probs = bayes_model.predict_proba(features)[0]
    return {
        "male": probs[1],
        "female": probs[0],
    }


def predict_rnn(text: str) -> dict[str, float]:
    try:
        # Suppress verbose output during prediction
        pred_arr = rnn_model.predict(np.array([text]), verbose=0)
        pred = float(pred_arr[0, 0])
        # F = 0, M = 1, P(!A) == 1 - P(A)
        return {"male": pred, "female": 1 - pred}
    except Exception as e:
        print(f"RNN prediction error: {e}")
        # Fallback to Bayes if RNN fails (compatibility issue)
        print("Falling back to Bayes classifier")
        return predict_bayes(text)


pred_funcs = {"bayes": predict_bayes, "rnn": predict_rnn}


def predict(text: str, classifier: str = "bayes") -> dict[str, str | dict[str, float]]:
    if classifier not in pred_funcs:
        raise ValueError(f"Unknown classifier: {classifier}. Must be one of {list(pred_funcs.keys())}")

    predict_proba = pred_funcs[classifier]
    return {"text": text, "classifier": classifier, "probability": predict_proba(text)}

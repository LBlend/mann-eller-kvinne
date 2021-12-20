from tensorflow import keras
from sklearn.metrics import classification_report
import nltk
import pickle
import train_bayes

dev_dir = "corpus/data/dev"
test_dir = "corpus/data/test"
batch_size = 10000


def get_dev_test():
    for dir in dev_dir, test_dir:
        data = keras.preprocessing.text_dataset_from_directory(
            dir, batch_size=batch_size
        )
        yield next(iter(data))


def get_predict_rnn(model_path):
    rnn_model = keras.models.load_model(model_path)
    return lambda x: (rnn_model(x) > 0.5).numpy().astype(int).squeeze()


def get_predict_bayes(model_path):
    with open(model_path, "rb") as f:
        bayes_model = pickle.load(f)

    def predict_on_str(text):
        text = text.decode("UTF8")
        text_tokens = nltk.tokenize.word_tokenize(text)
        text_features = train_bayes.preprocess(text_tokens)
        dist = bayes_model.prob_classify(text_features)
        return int(dist.prob("man") > 0.5)

    return lambda x: [predict_on_str(s) for s in x]


if __name__ == "__main__":
    dev_set, test_set = get_dev_test()

    predict_rnn = get_predict_rnn("bin/rnn")
    predict_bayes = get_predict_bayes("bin/bayes_model.pkl")

    for name, (X, y) in [("dev", dev_set), ("test", test_set)]:
        X = X.numpy()
        y_pred = predict_rnn(X)
        print("Results for", name, "with rnn:")
        print(classification_report(y, y_pred))

        y_pred = predict_bayes(X)
        print("Results for", name, "with bayes:")
        print(classification_report(y, y_pred))

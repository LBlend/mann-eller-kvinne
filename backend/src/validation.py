import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import classification_report
import nltk
import pickle
from scripts import train_bayes

if __name__ == '__main__':    
    train_dir = '../corpus/data/train'
    dev_dir = '../corpus/data/dev'
    test_dir = '../corpus/data/test'

    model = keras.models.load_model('../bin/rnn')
    dev = keras.preprocessing.text_dataset_from_directory(dev_dir, batch_size=10000)
    test = keras.preprocessing.text_dataset_from_directory(test_dir, batch_size=10000)

    dev_set = next(iter(dev))
    test_set = next(iter(test))

    X_dev, y_dev = dev_set
    X_test, y_test = test_set
    get_predictions = lambda x: (x > 0.5).numpy().astype(int).squeeze()

    dev_pred = get_predictions(model(X_dev))
    test_pred = get_predictions(model(X_test))
    print(classification_report(y_dev, dev_pred))
    print(classification_report(y_test, test_pred))


    with open('../bin/bayes_model.pkl', 'rb') as f:
        bayes = pickle.load(f)


    def predict_on_str(text):
        text = text.decode("UTF8")
        text_tokens = nltk.tokenize.word_tokenize(text)
        text_features = train_bayes.preprocess(text_tokens)
        dist = bayes.prob_classify(text_features)
        return int(dist.prob("man") > 0.5)

    dev_pred = [predict_on_str(s) for s in X_dev.numpy()]
    test_pred = [predict_on_str(s) for s in X_test.numpy()]
    print(classification_report(y_dev, dev_pred))
    print(classification_report(y_test, test_pred))

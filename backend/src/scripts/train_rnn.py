import tensorflow as tf
from tensorflow import keras
import numpy as np

train_dir = 'corpus/data/train'
dev_dir = 'corpus/data/dev'
test_dir = 'corpus/data/test'

batch_size = 32
buffer_size = 10000
seed = 42
VOCAB_SIZE = 1000

def load_datasets():
    train = keras.preprocessing.text_dataset_from_directory(
        train_dir,
        batch_size=batch_size)

    dev = keras.preprocessing.text_dataset_from_directory(
        dev_dir,
        batch_size=batch_size)

    return train, dev


def get_model(train_set):
    encoder = keras.layers.experimental.preprocessing.TextVectorization(
        max_tokens=VOCAB_SIZE)

    encoder.adapt(train_set.map(lambda text, label: text))

    model = tf.keras.Sequential([
        encoder,
        tf.keras.layers.Embedding(
            input_dim=len(encoder.get_vocabulary()),
            output_dim=64,
            mask_zero=True),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(loss=tf.keras.losses.BinaryCrossentropy(),
                  optimizer=tf.keras.optimizers.Adam(1e-4),
                  metrics=['accuracy'])

    return model


def train(path):
    # Set global seed for reproducibility
    tf.random.set_seed(seed)

    raw_train_ds, raw_dev_ds = load_datasets()

    model = get_model(raw_train_ds)

    history = model.fit(raw_train_ds, epochs=10,
                        validation_data=raw_dev_ds,
                        validation_steps=10)

    model.save(path)

    return model


if __name__ == '__main__':
    train('bin/rnn')

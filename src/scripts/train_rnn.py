# import numpy as np
from tensorflow import keras
import tensorflow as tf


TRAIN_DIR = "corpus/data/train"
DEV_DIR = "corpus/data/dev"
TEST_DIR = "corpus/data/test"

BATCH_SIZE = 32
BUFFER_SIZE = 10000
SEED = 42
VOCAB_SIZE = 1000


def load_datasets() -> tuple[tf.data.Dataset, tf.data.Dataset]:
    train = keras.preprocessing.text_dataset_from_directory(
        TRAIN_DIR, batch_size=BATCH_SIZE
    )
    dev = keras.preprocessing.text_dataset_from_directory(
        DEV_DIR, batch_size=BATCH_SIZE
    )

    return train, dev


def get_model(train_set: tf.data.Dataset) -> keras.Model:
    encoder = keras.layers.experimental.preprocessing.TextVectorization(
        max_tokens=VOCAB_SIZE
    )
    encoder.adapt(train_set.map(lambda text: text))

    model = tf.keras.Sequential(
        [
            encoder,
            tf.keras.layers.Embedding(
                input_dim=len(encoder.get_vocabulary()), output_dim=64, mask_zero=True
            ),
            tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )
    model.compile(
        loss=tf.keras.losses.BinaryCrossentropy(),
        optimizer=tf.keras.optimizers.Adam(1e-4),
        metrics=["accuracy"],
    )

    return model


def train(path: str) -> keras.Model:
    tf.random.set_seed(SEED)  # Set global seed for reproducibility

    raw_train_ds, raw_dev_ds = load_datasets()
    model = get_model(raw_train_ds)
    model.fit(raw_train_ds, epochs=10, validation_data=raw_dev_ds, validation_steps=10)
    model.save(path)

    return model


if __name__ == "__main__":
    train("bin/rnn")

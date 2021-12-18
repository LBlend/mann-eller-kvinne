import numpy as np
from argparse import ArgumentParser
import yaml
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"
import tensorflow as tf  # noqa: E402


TRAIN_DIR = "corpus/data/train"
DEV_DIR = "corpus/data/dev"
# TEST_DIR = 'corpus/data/test'


def load_datasets(batch_size):
    train = tf.keras.preprocessing.text_dataset_from_directory(
        TRAIN_DIR, batch_size=batch_size
    )

    dev = tf.keras.preprocessing.text_dataset_from_directory(
        DEV_DIR, batch_size=batch_size
    )

    return train, dev


def get_optimizer(name, optimizer_args={}):
    options = {
        "Adam": tf.keras.optimizers.Adam,
        "RMSProp": tf.keras.optimizers.RMSprop,
        "SGD": tf.keras.optimizers.SGD,
    }

    constructor = options.get(name)

    if not constructor:
        raise TypeError(f"Invalid optimizer: {name}")
    else:
        return constructor(**optimizer_args)


def get_model(train_set, config):
    shapes = config["model_shapes"]

    encoder = tf.keras.layers.experimental.preprocessing.TextVectorization(
        max_tokens=shapes["vocab_size"]
    )

    encoder.adapt(train_set.map(lambda text, label: text))

    lstm = tf.keras.layers.LSTM(shapes["lstm"])

    if config["bidirectional"]:
        lstm = tf.keras.layers.Bidirectional(lstm)

    model = tf.keras.Sequential(
        [
            encoder,
            tf.keras.layers.Embedding(
                input_dim=len(encoder.get_vocabulary()),
                output_dim=shapes["embedding"],
                mask_zero=True,
            ),
            lstm,
            tf.keras.layers.Dense(shapes["dense"], activation="relu"),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )

    model.compile(
        loss=tf.keras.losses.BinaryCrossentropy(),
        optimizer=get_optimizer(config["optimizer_type"], config["optimizer_args"]),
        metrics=["accuracy"],
    )

    return model


def get_train_callbacks(config):
    train_callbacks = []

    early_stopper_args = config.get("early_stopper")
    if early_stopper_args:
        early_stopper = (tf.keras.callbacks.EarlyStopping(**early_stopper_args),)
        train_callbacks.append(early_stopper)

    if config.get("log_folder"):
        log_path = f'logs/{config["log_folder"]}/'
        tb_callback = tf.keras.callbacks.TensorBoard(log_dir=log_path)
        train_callbacks.append(tb_callback)

    return train_callbacks


def train(config):
    output_path = f'bin/{config["output_folder"]}'

    # Set global seed for reproducibility
    np.random.seed(config.get("random_seed"))
    tf.random.set_seed(config.get("random_seed"))

    raw_train_ds, raw_dev_ds = load_datasets(batch_size=config["batch_size"])

    model = get_model(raw_train_ds, config)

    train_callbacks = get_train_callbacks(config)

    model.fit(
        raw_train_ds,
        epochs=config["epochs"],
        validation_data=raw_dev_ds,
        callbacks=train_callbacks,
    )

    model.save(output_path)

    return model


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("config", nargs="?", default="rnn_default.yaml")
    args = parser.parse_args()

    with open(f"configs/{args.config}") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    # Allows use of scientific notation
    config["optimizer_args"]["learning_rate"] = float(
        config["optimizer_args"]["learning_rate"]
    )

    print("\n".join(f"{k}: {v}" for k, v in config.items()))
    train(config)

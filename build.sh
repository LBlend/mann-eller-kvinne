#!/bin/sh
set -e

echo "Installing Python dependencies..."
uv sync --frozen

if [ ! -d 'corpus' ]; then
    echo "Downloading corpus..."
    git clone --depth 1 https://github.com/ltgoslo/norec_gender.git corpus
    uv run python ./src/scripts/organize_corpus.py
    uv run python ./src/scripts/clean_data.py
fi

echo "Downloading NLTK stopwords..."
uv run python -c "import nltk; nltk.download('stopwords')"

if [ ! -e 'src/bin/bayes_model_sk.pkl' ] || [ ! -e 'src/bin/vectorizer.pkl' ]; then
    echo "Training Bayes model..."
    uv run python ./src/scripts/train_bayes.py
fi

if [ ! -e 'src/bin/rnn.keras' ]; then
    echo "Training RNN model..."
    uv run python ./src/scripts/train_rnn.py
fi

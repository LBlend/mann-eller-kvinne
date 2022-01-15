#!/bin/sh

echo "Installing Python dependencies..."
python3 -m pip install -r requirements.txt -U

if [ ! -d 'corpus' ]; then
    echo "Downloading corpus..."
    mkdir corpus
    git clone https://github.com/ltgoslo/norec_gender.git corpus
    python3 ./src/scripts/organize_corpus.py
    python3 ./src/scripts/clean_data.py
fi

echo "Downloading NLTK stopwords and punctuation packages..."
python3 -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"

if [ ! -e 'bin/bayes_model.pkl' ]; then
    echo "Training Bayes model..."
    python3 ./src/scripts/train_bayes.py
fi

if [ ! -d 'bin/rnn' ]; then
    echo "Training RNN model..."
    python3 ./src/scripts/train_rnn.py
fi

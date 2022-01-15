#!/bin/sh

python3 -m pip install -r requirements.txt -U

if [ ! -d 'corpus' ]; then
    mkdir corpus
    git clone https://github.com/ltgoslo/norec_gender.git corpus
    python3 ./src/scripts/organize_corpus.py
    python3 ./src/scripts/clean_data.py
fi

python3 -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"

if [ ! -e 'bin/bayes_model.pkl' ]; then
    python3 ./src/scripts/train_bayes.py
fi

if [ ! -d 'bin/rnn' ]; then
    python3 ./src/scripts/train_rnn.py
fi

#!/bin/sh

if [ ! -d 'corpus' ]; then
    mkdir corpus
    git clone https://github.com/ltgoslo/norec_gender.git corpus
fi

python3 -m pip install -r requirements.txt
python3 ./src/model/corpus_parser.py
python3 ./src/model/trainer.py

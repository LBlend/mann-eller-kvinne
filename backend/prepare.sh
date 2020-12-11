#!/bin/sh

python3 -m pip install -r requirements.txt
python3 ./src/model/corpus_paser.py
python3 ./src/model/trainer.py
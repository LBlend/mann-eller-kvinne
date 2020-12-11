from json import load
import os
from shutil import copy


corpus_raw_path = './corpus/NoRec_gender_raw'
corpus_parsed_path = './corpus/NoRec_gender'

def init_parsed_corpus():
    try:
        os.mkdir(corpus_parsed_path)
    except FileExistsError:
        pass

    classes = ['M', 'F']
    for c in classes:
        try:
            os.mkdir(f'{corpus_parsed_path}/{c}')
        except FileExistsError:
            pass


def main():
    with open(f'{corpus_raw_path}/metadata_norec_gender.json', 'r', encoding='utf-8') as f:
        metadata = load(f)

    for entry in metadata:
        gender = metadata[entry]['gender_critics'][0]
        if gender != 'M' and gender != 'F':
            continue
        if f'{entry}.txt' in os.listdir(f'{corpus_raw_path}/train'):
            print(f'Copying {corpus_raw_path}/train/{entry}.txt -> {corpus_parsed_path}/{gender}/{entry}.txt')
            copy(f'{corpus_raw_path}/train/{entry}.txt', f'{corpus_parsed_path}/{gender}/{entry}.txt')


if __name__ == '__main__':
    init_parsed_corpus()
    main()
    print('\nFINISHED')

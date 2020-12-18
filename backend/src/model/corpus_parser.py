import json
import os
import shutil
from tqdm import tqdm

corpus_raw_path = './corpus/data'
corpus_parsed_path = './corpus'


classes = ['M', 'F']


def main():
    for c in classes:
        try:
            print(f'Making directory corpus/{c}\n')
            os.mkdir(f'{corpus_parsed_path}/{c}')
        except FileExistsError:
            pass

    with open(f'{corpus_raw_path}/metadata_norec_gender.json', 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    for entry in tqdm(metadata, desc='Copying data'):
        gender = metadata[entry]['gender_critics'][0]
        if gender in classes:
            if f'{entry}.txt' in os.listdir(f'{corpus_raw_path}/train'):
                shutil.copy(f'{corpus_raw_path}/train/{entry}.txt', f'{corpus_parsed_path}/{gender}/{entry}.txt')


if __name__ == '__main__':
    main()

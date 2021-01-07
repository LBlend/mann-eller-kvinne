import json
import os
import shutil
from tqdm import tqdm
# from collections import Counter

corpus_data = './corpus/data'

classes = []
splits = ('train', 'dev', 'test')


def main():
    with open(f'{corpus_data}/metadata_norec_gender.json', 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    for entry, content in tqdm(metadata.items(), desc='Organizing data by label'):
        gender, *_ = genders = content['gender_critics']

        if len(genders) > 1:
            # gender, = Counter(genders).most_common(1)[0]
            gender = 'MULTI_AUTHOR'

        split = content['split']
        if gender not in classes:
            for s in splits:
                try:
                    os.mkdir(f'{corpus_data}/{s}/{gender}')
                except FileExistsError:
                    pass

                classes.append(gender)

        try:
            shutil.move(f'{corpus_data}/{split}/{entry}.txt', f'{corpus_data}/{split}/{gender}/{entry}.txt')
        except FileNotFoundError as e:
            print(e)


if __name__ == '__main__':
    main()

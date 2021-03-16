import os
import shutil
from contexlib import suppress

data_path = './corpus/data'

splits = ('train', 'dev', 'test')

new_dir = f'{data_path}/ETC'


def move_etc_data():
    with suppress(FileExistsError):
        os.mkdir(new_dir)

    for s in splits:
        cur_path = f'{data_path}/{s}'
        for i in os.listdir(cur_path):
            if i not in {'M', 'F'}:
                shutil.move(f'{cur_path}/{i}', f'{new_dir}/{s}')


if __name__ == "__main__":
    move_etc_data()

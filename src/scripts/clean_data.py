import os
import shutil


DATA_PATH = "./corpus/data"
SPLITS = ("train", "dev", "test")
NEW_DIR = f"{DATA_PATH}/ETC"


def move_etc_data() -> None:
    try:
        os.mkdir(NEW_DIR)
    except FileExistsError:
        pass

    for s in SPLITS:
        cur_path = f"{DATA_PATH}/{s}"
        for i in os.listdir(cur_path):
            if i not in {"M", "F"}:
                shutil.move(f"{cur_path}/{i}", f"{NEW_DIR}/{s}")


if __name__ == "__main__":
    move_etc_data()

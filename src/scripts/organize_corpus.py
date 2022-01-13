# from collections import Counter
import json
import os
import shutil
from tqdm import tqdm


CORPUS_DATA_PATH = "./corpus/data"
SPLITS = ("train", "dev", "test")
classes = []


def main() -> None:
    with open(
        f"{CORPUS_DATA_PATH}/metadata_norec_gender.json", "r", encoding="utf-8"
    ) as f:
        metadata = json.load(f)

    for entry, content in tqdm(metadata.items(), desc="Organizing data by label"):
        gender, *_ = genders = content["gender_critics"]

        if len(genders) > 1:
            # gender, = Counter(genders).most_common(1)[0]
            gender = "MULTI_AUTHOR"

        split = content["split"]
        if gender not in classes:
            for s in SPLITS:
                try:
                    os.mkdir(f"{CORPUS_DATA_PATH}/{s}/{gender}")
                except FileExistsError:
                    pass

                classes.append(gender)

        try:
            shutil.move(
                f"{CORPUS_DATA_PATH}/{split}/{entry}.txt",
                f"{CORPUS_DATA_PATH}/{split}/{gender}/{entry}.txt",
            )
        except FileNotFoundError as e:
            print(e)


if __name__ == "__main__":
    main()

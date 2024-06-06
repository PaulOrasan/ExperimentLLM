import pandas as pd
from typing import Dict, List

from entity.dataset import Dataset

AVAILABLE_DATASETS = [Dataset("gsm8k-ro", ["train", "test"]), Dataset("gsm8k-ro", ["train", "test"]), Dataset("gsm8k-ro", ["train", "test"])]


def fetch_available_datasets() -> List[Dataset]:
    return AVAILABLE_DATASETS


def fetch_dataset(dataset_name, split) -> pd.DataFrame:
    return pd.read_csv(f"{dataset_name}/{split}.csv", usecols=[0, 1], quotechar='"')


if __name__ == "__main__":
    df = fetch_dataset("../gsm8k-ro", "train")
    print()
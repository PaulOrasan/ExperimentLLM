from dataclasses import dataclass
from typing import List


@dataclass(eq=True, frozen=True)
class Dataset:
    dataset_name: str
    splits: List[str]
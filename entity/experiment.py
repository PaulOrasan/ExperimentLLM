from dataclasses import dataclass

from entity.dataset import Dataset
from entity.model import Model


@dataclass(frozen=True, eq=True)
class Experiment:
    dataset: Dataset
    model: Model
    results_file: str


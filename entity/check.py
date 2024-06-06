from dataclasses import dataclass
from typing import List, Union

from entity.experiment import Experiment
from entity.model import Model


@dataclass
class Check:
    question: str
    is_accurate: Union[bool, None]


@dataclass
class Evaluation:
    experiment: Experiment
    checks: List[Check]
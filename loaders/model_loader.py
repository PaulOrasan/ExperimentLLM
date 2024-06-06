from typing import List

from entity.model import Model

AVAILABLE_MODELS = [Model("RoLlama2-base"), Model("RoLlama2-finetuned")]


def fetch_available_models() -> List[Model]:
    return AVAILABLE_MODELS

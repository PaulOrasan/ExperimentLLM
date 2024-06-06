from typing import List

from entity.model import Model

AVAILABLE_MODELS = [Model("RoLlama2-base"), Model("RoLlama2-finetuned")]


def fetch_available_models() -> List[Model]:
    return AVAILABLE_MODELS


def fetch_response_from_model(model: Model, chat_history: List[str], user_message: str) -> str:
    return f"You said {user_message}!"

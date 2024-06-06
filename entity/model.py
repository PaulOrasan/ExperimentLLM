from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Model:
    model_name: str


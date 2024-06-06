from typing import List

from entity.dataset import Dataset
from entity.experiment import Experiment
from entity.model import Model

dataset = Dataset("gsm8k-ro", ["train", "test"])
rollama_base = Model("RoLLaMa2-instr")
rollama_finetuned = Model("RoLLaMa2-instr-fine-tuned")

AVAILABLE_EXPERIMENTS = [Experiment(dataset, rollama_base, "rollama2-instr-base.txt"), Experiment(dataset, rollama_finetuned, "rollama2-instr-finetuned.txt")]
cache = {}

def fetch_available_experiments() -> List[Experiment]:
    if len(cache) != 0:
        return AVAILABLE_EXPERIMENTS
    for exp in AVAILABLE_EXPERIMENTS:
        local_cache = {}
        with open("experiments/" + exp.results_file, "r", encoding="utf8") as f:
            question = ""
            answer = ""
            lines = f.readlines()
            i = 0
            while i < len(lines):
                if lines[i].startswith("QUESTION:"):
                    question = lines[i + 1].strip()
                    i += 2
                    continue
                if lines[i].startswith("PREDICTED ANSWER:"):
                    i += 1
                    answer = ""
                    while i < len(lines) and not lines[i].startswith("GROUND ANSWER:"):
                        answer += lines[i]
                        i += 1
                    local_cache[question] = answer
                i += 1
        cache[exp.dataset.dataset_name + exp.model.model_name] = local_cache
    return AVAILABLE_EXPERIMENTS


def fetch_experiment_prediction(exp: Experiment, question: str):
    return cache[exp.dataset.dataset_name + exp.model.model_name][question.strip()]


def fetch_available_questions(exp: Experiment):
    return list(cache[exp.dataset.dataset_name + exp.model.model_name].keys())


if __name__ == "__main__":
    fetch_available_experiments()
    print()
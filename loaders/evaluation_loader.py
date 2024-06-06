from typing import List

from entity.check import Evaluation, Check
from entity.experiment import Experiment
from loaders.experiment_loader import fetch_available_experiments, fetch_available_questions

experiments = fetch_available_experiments()
AVAILABLE_EVALUATIONS = [Evaluation(experiment, []) for experiment in experiments]


def load_checks_from_file(filename: str) -> List[Check]:
    checks = []
    with open(filename, "r", encoding="utf8") as f:
        i = 0
        lines = f.readlines()
        while i < len(lines):
            question = lines[i]
            if lines[i + 1] == "\n":
                checks.append(Check(question, None))
            else:
                is_accurate = lines[i + 1].strip() == "True"
                checks.append(Check(question, is_accurate))
            i += 2
    return checks


def save_checks_to_file(filename: str, checks: List[Check]):
    with open(filename, "w", encoding="utf8") as f:
        for check in checks:
            f.write(check.question)
            if check.is_accurate is not None:
                f.write(str(check.is_accurate) + "\n")
            else:
                f.write("\n")


def build_eval_filename(results_file: str) -> str:
    return "experiments/" + results_file + "_eval.txt"


def fetch_available_evaluations():
    for evaluation in AVAILABLE_EVALUATIONS:
        evaluation.checks = load_checks_from_file(build_eval_filename(evaluation.experiment.results_file))
    return AVAILABLE_EVALUATIONS


def add_evaluation(exp: Evaluation, question: str, is_accurate: bool):
    for check in exp.checks:
        if check.question == question:
            check.is_accurate = is_accurate
    save_checks_to_file(build_eval_filename(exp.experiment.results_file), exp.checks)


if __name__ == "__main__":
    # fetch_available_evaluations()
    for eval in AVAILABLE_EVALUATIONS:
        qs = fetch_available_questions(eval.experiment)
        with open(build_eval_filename(eval.experiment.results_file), "w", encoding="utf8") as f:
            for q in qs:
                f.write(q + "\n")
                f.write("\n")
    print()

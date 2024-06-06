import gradio as gr
import pandas as pd
from loaders.evaluation_loader import fetch_available_evaluations, add_evaluation
from loaders.experiment_loader import fetch_available_experiments, fetch_experiment_prediction
import matplotlib.pyplot as plt

evaluations = fetch_available_evaluations()


def on_question_change(index):
    question = evaluations[0].checks[index].question
    predictions = [fetch_experiment_prediction(ev.experiment, question) for ev in evaluations]
    checkboxes = [True if ev.checks[index].is_accurate else False for ev in evaluations]
    return [question] + predictions + checkboxes


def on_validate_click(question, *checkbox_inputs):
    for ev, ch in zip(evaluations, checkbox_inputs):
        add_evaluation(ev, question, ch)


def build_accuracy_plot():
    accuracies = []
    for evaluation in evaluations:
        statuses = list(filter(lambda x: x.is_accurate is not None, evaluation.checks))
        if not statuses:
            accuracies.append(0)
            continue
        accuracies.append(len(list(filter(lambda x: x.is_accurate == True, statuses))) / len(statuses) * 100)
    plt.close()
    fig = plt.figure()
    plt.bar([ev.experiment.model.model_name for ev in evaluations], accuracies, color=["red", "purple"])
    plt.ylim(0, 100)
    plt.ylabel("Accuracy")
    plt.title("Accuracy of models")
    return fig


def build_annotation_plot():
    statuses = list(filter(lambda x: x.is_accurate is not None, evaluations[0].checks))
    plt.close()
    fig = plt.figure()
    plt.pie([len(statuses), len(evaluations[0].checks) - len(statuses)], labels=["Verified", "Not Verified"])
    plt.title("Percentage of validation")
    plt.legend()
    return fig


def get_next_not_validated(index):
    index += 1
    while index < len(evaluations[0].checks):
        if evaluations[0].checks[index].is_accurate is None:
            return index
        index += 1
    return 0


def create_tab():
    with gr.TabItem("Experiment Viewer", id=1) as tab:
        selected_question = gr.State(-1)
        with gr.Column():
            with gr.Row():
                gr.Button("Previous question").click(lambda index: index - 1, inputs=[selected_question],
                                                     outputs=[selected_question])
                gr.Button("Next question").click(lambda index: index + 1, inputs=[selected_question],
                                                 outputs=[selected_question])
                gr.Button("Next not validated question").click(get_next_not_validated, inputs=[selected_question],
                                                               outputs=[selected_question])
            question_box = gr.Textbox(label="Question")
            model_output_textboxes = []
            is_accurate_checkboxes = []
            for ev in evaluations:
                with gr.Row():
                    box = gr.Textbox(label=ev.experiment.model.model_name, scale=6)
                    chbox = gr.Checkbox(label="Accurate?", scale=1)
                    model_output_textboxes.append(box)
                    is_accurate_checkboxes.append(chbox)
            gr.Button("Validate predictions!").click(on_validate_click, inputs=[question_box] + is_accurate_checkboxes)
            selected_question.change(on_question_change, inputs=[selected_question],
                                     outputs=[question_box] + model_output_textboxes + is_accurate_checkboxes)

            with gr.Row():
                gr.Plot(build_accuracy_plot, every=10, scale=1)
                gr.Plot(build_annotation_plot, every=10, scale=1)
    return tab

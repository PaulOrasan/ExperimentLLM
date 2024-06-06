import time

import gradio as gr

from loaders.data_loader import fetch_available_datasets, fetch_dataset
from loaders.experiment_loader import fetch_available_experiments, fetch_experiment_prediction

datasets = fetch_available_datasets()
experiments = fetch_available_experiments()


def on_dataset_dropdown_change(event: gr.SelectData, progress=gr.Progress()):
    dataset = datasets[event.index]
    progress(0, desc=f"Identifying dataset {dataset.dataset_name}...")
    time.sleep(2)
    progress(0.25, desc="Found dataset! Downloading...")
    time.sleep(3)
    progress(0.5, desc="Dataset fairly large, thank you for your patience!")
    time.sleep(3)
    progress(0.8, desc="Almost done!")
    time.sleep(2)
    return fetch_dataset(dataset.dataset_name, dataset.splits[0])


def on_split_dropdown_change(data_index, event: gr.SelectData):
    dataset = datasets[data_index]
    return fetch_dataset(dataset.dataset_name, event.value)


def on_dataset_change(data, event: gr.SelectData):
    row = data.iloc[event.index[0]]
    return row[0], row[1]


def create_tab():
    with gr.TabItem("Data Viewer", id=0) as tab:
        with gr.Column():
            with gr.Row():
                dataset_dropdown = gr.Dropdown([d.dataset_name for d in datasets], type="index",
                                               label="Select dataset:")
                split_dropdown = gr.Dropdown(["train", "test"], label="Select split:", value="train")

            dataframe = gr.DataFrame(headers=["Question", "Answer"], label="View data:")
            question_box = gr.Textbox(label="Question:")
            answer_box = gr.Textbox(label="Answer:")

            dataset_dropdown.select(on_dataset_dropdown_change, inputs=[], outputs=[dataframe])
            split_dropdown.select(on_split_dropdown_change, inputs=[dataset_dropdown], outputs=[dataframe])
            dataframe.select(on_dataset_change, inputs=[dataframe], outputs=[question_box, answer_box])
    return tab

import gradio as gr

from app_data_model_viewer import create_tab as create_data_viewer_tab
from app_experiment_viewer import create_tab as create_experiment_viewer_tab
from app_chat import create_tab as create_chat_tab

allowed_users = [("Paul", "parola"), ("Anca", "parola")]
theme = gr.themes.Soft(
    primary_hue="rose",
    secondary_hue="fuchsia",
)

if __name__ == "__main__":
    with gr.Blocks(theme=theme) as demo:
        with gr.Row():
            gr.Markdown("# Experiment with LLMs!")
            logout_button = gr.Button("Logout", link="/logout")
        with gr.Tabs() as tabs:
            create_data_viewer_tab()
            create_experiment_viewer_tab()
            create_chat_tab()
    demo.launch(auth=allowed_users)
import time

import gradio as gr

from loaders.model_loader import fetch_available_models, fetch_response_from_model

models = fetch_available_models()


def on_model_change(selected_model, history_by_model):
    return history_by_model[selected_model]


def respond(message, chat_history, selected_model, history_by_model, request: gr.Request):
    bot_message = fetch_response_from_model(models[0], chat_history, message, request.username)
    chat_history.append((message, bot_message))
    history_by_model[selected_model] = chat_history
    time.sleep(2)
    return "", chat_history, history_by_model


def create_tab():
    with gr.TabItem("Chat with AI", id=2) as tab:
        history_by_model = gr.State({model.model_name:[] for model in models})
        selected_model = gr.Dropdown(choices=[model.model_name for model in models], value=models[0].model_name, label="Model")
        chatbot = gr.Chatbot(min_width=500)
        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])

        msg.submit(respond, [msg, chatbot, selected_model, history_by_model], [msg, chatbot, history_by_model])
        selected_model.change(on_model_change, inputs=[selected_model, history_by_model], outputs=[chatbot])
    return tab

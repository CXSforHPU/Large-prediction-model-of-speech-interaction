"""
作者 河南理工大学 曹显嵩
    本文件半成品
    为以后的优化方向

"""



import gradio as gr
import random
import time
from tools import ai
app = ai()

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()

    with gr.Row():
        msg = gr.Textbox()

        audio = gr.Audio()

    clear = gr.Button("清除")



    def user(user_message, history):


        return "", history + [[user_message, None]]


    def bot(history):
        user_meassage = history[-1][0]
        if user_meassage[0] == '/':
            user_meassage = user_meassage[1:]
            bot_message = app.translater_object.translate(user_meassage)
        else:
            bot_message = app.deal(user_meassage)

        history[-1][1]= bot_message
        yield history





    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

demo.queue()
demo.launch()

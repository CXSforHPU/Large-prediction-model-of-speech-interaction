"""
作者 :河南理工大学 曹显嵩
    河南理工大学 吴锡煐
此文件仅仅支持自定义的翻译智能体
其他自定义智能体 在翻译文件方面 暂不全面支持

联系方式: qq:3130939083
微信 :c3130939083

"""
from tools import ai
import gradio as gr
from text import audio_text



# 实例化AI类
app = ai()

def process_and_respond(input_text, uploaded_file=None,audio_input=None):
    response_text = None
    audio_file_path = None
    translated_file_path = None  # 新增变量，用于存储翻译后的文件路径
    if not audio_input:
        if uploaded_file is not None:
            file_path = uploaded_file.name
            if file_path.endswith('.docx'):
                file_path_translated = app.file_to_file(file_path)  # 翻译文件
                summary_text = app.Summary_to_text(file_path_translated)  # 获取文件总结
                response_text = summary_text

                audio_file_path = app.text_to_speech(response_text)
                translated_file_path = file_path_translated  # 设置翻译后的文件路径
            else:
                response_text = "不支持的文件类型。目前仅支持.docx文件。"

                audio_file_path = app.text_to_speech(response_text)
        else:
            t = str(input_text)
            if t[0] == '/':
                t = t[1:]
                input_text = app.translater_object.translate(t)
                response_text = input_text

            else:
                response_text = app.deal(input_text)

            audio_file_path = app.text_to_speech(response_text)
    else:
        # 设置音频文件的位置
        audio_file = audio_input

        text = audio_text(audio_file)

        response_text=app.deal(text)


        audio_file_path = app.text_to_speech(response_text)



    return response_text, audio_file_path, translated_file_path  # 返回翻译后的文件路径

iface = gr.Interface(
    fn=process_and_respond,
    inputs=[gr.Textbox(lines=2, placeholder="请输入问题..."), gr.File(label="上传文件"),gr.Audio(label='输入音频',type='filepath',sources="microphone")],
    outputs=[gr.Text(label="文本回答"), gr.Audio(label="音频回答", type="filepath",format='wav'), gr.File(label="翻译后的文件")],
    title="问答系统",
    description="请输入问题或上传文本文件，系统会提供回答并朗读。"
)


iface.launch(share=True)
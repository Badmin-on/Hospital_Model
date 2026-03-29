import gradio as gr
import os
from core.engine import HospitalOmniEngine

# Initialize Engine
engine = HospitalOmniEngine()

# Custom CSS for Premium Design
custom_css = """
body { background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; }
.container { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; }
button.primary { background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); border: none; border-radius: 10px; font-weight: 600; color: white; transition: all 0.3s; }
button.primary:hover { transform: scale(1.02); filter: brightness(1.1); }
"""

def process_folder(folder_path):
    if not os.path.isdir(folder_path):
        return "❌ 올바른 폴더 경로를 입력하세요."
    count = engine.index_folder(folder_path)
    return f"✅ {count}개의 문서 조각이 인덱싱되었습니다."

def chat_response(message, image, history):
    response = engine.chat(message, image)
    history.append((message, response))
    return "", history

with gr.Blocks(css=custom_css, title="hospital-Omni-V1 Hub") as demo:
    with gr.Column(elem_classes="container"):
        gr.Markdown("# 🏥 hospital-Omni-V1 : Premium Medical Hub")
        gr.Markdown("### 🛡️ 100% Offline Multi-Modal Analysis System")
        
        with gr.Row():
            folder_input = gr.Textbox(label="인덱싱할 폴더 경로", placeholder="D:/Documents/Medical")
            btn_index = gr.Button("분석 시작", elem_classes="primary")
        
        index_status = gr.Label(value="대기 중...")
        btn_index.click(process_folder, inputs=[folder_input], outputs=[index_status])
        
        with gr.Row():
            with gr.Column(scale=8):
                chatbot = gr.Chatbot(label="Omni Engine Chat")
                msg = gr.Textbox(label="질문", placeholder="증상이나 문서에 대해 질문하세요...")
                btn_send = gr.Button("질문 전송", elem_classes="primary")
            with gr.Column(scale=2):
                image_input = gr.Image(label="시각 분석 (X-ray/처방전)", type="filepath")
        
        history = gr.State([])
        btn_send.click(chat_response, inputs=[msg, image_input, history], outputs=[msg, chatbot])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)

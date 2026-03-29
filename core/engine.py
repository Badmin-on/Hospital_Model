import base64
import requests
import json
from core.vector_db import HospitalVectorDB

class HospitalOmniEngine:
    def __init__(self):
        self.model_name = "hospital-Omni-V1"
        self.vdb = HospitalVectorDB()
        self.ollama_url = "http://localhost:11434/api/generate"

    def chat(self, message, image_path=None):
        context_docs = self.vdb.search(message)
        context_text = "\n".join([f"[{d.metadata['source']}] {d.page_content}" for d in context_docs])
        
        prompt = f"아래 문서를 참고하여 답변하세요:\n{context_text}\n\n질문: {message}"
        
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }
        
        if image_path:
            with open(image_path, "rb") as f:
                img_data = base64.b64encode(f.read()).decode('utf-8')
                payload["images"] = [img_data]
                payload["prompt"] = f"이미지를 분석하고 아래 질문에 답하세요: {message}"

        response = requests.post(self.ollama_url, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "응답 생성 실패")
        else:
            return f"에러 발생: {response.text}"

    def index_folder(self, folder_path):
        return self.vdb.add_documents(folder_path)

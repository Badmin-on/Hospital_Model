# 🏥 hospital-Omni-V1 : Premium Medical AI Hub

> **"Extreme Efficiency, Unified Intelligence."**  
> 8GB RAM 및 GPU가 없는 환경에서도 작동하는 프리미엄 오프라인 의료 문서 분석 시스템.

---

## 🦅 Project Vision
**hospital-Omni-V1**은 Antigravity Hub 생태계의 압축 및 합성 기술력을 집약한 **'All-in-One 융합 모델'** 프로젝트입니다. 단순한 텍스트 분석을 넘어 이미지 분석(Vision)과 지식 추출(Embedding) 기능을 하나의 지능체로 통합하여, 의료 데이터의 보안과 성능을 동시에 확보합니다.

## ✨ Key Features
- **Neural Fusion**: `LLM + Vision + Embedding` 기능이 통합된 단일 신경망 구조.
- **Extreme Optimization**: 8GB RAM, CPU-Only 환경(내장 그래픽)에서도 안정적인 추론.
- **Premium Localhost UI**: 글래스모피즘 테마의 세련된 웹 인터페이스 제공.
- **100% Offline & Private**: 모든 데이터는 로컬 RAM 내에서만 처리되어 유출 위험 제로.
- **Source-Cited RAG**: 답변 시 반드시 근거 문서의 파일명과 페이지 번호를 표기.

---

## 💻 권장 PC 사양 (System Requirements)
| 항목 | 최소 사양 | 권장 사양 |
|---|---|---|
| **CPU** | 4-Core (Intel 7th Gen 이상) | 8-Core 이상 |
| **RAM** | **8 GB** (여유 공간 4GB+) | 16 GB 이상 |
| **GPU** | 필요 없음 (CPU 추론 최적화) | NVIDIA GPU (선택 사항) |
| **OS** | Windows 10/11, Linux, macOS | 동일 |

---

## 🚀 시작하기 (Getting Started)

### 1. 전제 조건 (Prerequisites)
- [Ollama](https://ollama.ai/) 설치 필수.
- Python 3.10 이상 설치.

### 2. 모델 준비 (Neural Engine Setup)
터미널에서 아래 명령을 실행하여 베이스 모델을 준비하고 전용 페르소나를 생성합니다.
```bash
# 베이스 멀티모달 모델 다운로드
ollama pull qwen3-vl:4b

# hospital-Omni-V1 고유 모델 생성
ollama create hospital-Omni-V1 -f Modelfile
```

### 3. 설치 및 실행 (Installation)
```bash
# 리포지토리 클론
git clone https://github.com/Badmin-on/Hospital_Model.git
cd Hospital_Model

# 가상환경 구축 및 패키지 설치
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 원클릭 실행 (Windows 전용)
./start_hub.bat
```

---

## 🎨 Design & Architecture
- **Framework**: LangChain, Gradio, ChromaDB (Vector Store).
- **Core Model**: `hospital-Omni-V1` (Fused with Vision & Medical System Prompt).
- **Embedding**: `BAAI/bge-m3` (High-density Semantic Mapping).

---

## 🤝 Contribution & License
본 프로젝트는 **MIT License**에 따라 자유롭게 사용 및 수정이 가능합니다.  
제작: **JARVIS & Antigravity Hub (Alex Commander Group)**

---
*Precision is the bridge between inspiration and reality.*

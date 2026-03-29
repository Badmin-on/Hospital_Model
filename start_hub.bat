@echo off
setlocal enabledelayedexpansion
pushd "%~dp0"

echo [1/5] Checking Environment...
if not exist venv (
    echo [*] Virtual environment not found. Creating venv...
    python -m venv venv
    call venv\Scripts\activate
    echo [*] Installing dependencies (this may take a few minutes)...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate
)

echo [2/5] Checking Ollama Service...
ollama list >nul 2>&1
if int(!errorlevel!) neq 0 (
    echo [ERROR] Ollama is not running! Please install and start Ollama (https://ollama.com).
    pause
    exit /b
)

echo [3/5] Checking hospital-Omni-V1 Model...
ollama list | findstr "hospital-omni-v1" >nul
if !errorlevel! neq 0 (
    echo [*] Model 'hospital-omni-v1' not found. Registering...
    ollama create hospital-omni-v1 -f Modelfile
)

echo [4/5] Preparing Medical Vector Nexus...
if not exist chroma_db mkdir chroma_db

echo [5/5] Launching hospital-Omni-V1 Hub at http://localhost:7860
python app.py
pause
popd

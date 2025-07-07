FROM python:3.10-slim

# Evita bytecode e melhora logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instalações do sistema necessárias para whisper, ffmpeg, etc
RUN apt update && apt install -y \
    ffmpeg \
    libsndfile1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia apenas o requirements.txt e instala as dependências primeiro (melhora cache)
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip \
    && pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu \
    && pip install -r requirements.txt

# Copia o restante do código do projeto
COPY . /app

# Expõe porta padrão do FastAPI
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

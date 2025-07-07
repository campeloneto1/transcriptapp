FROM python:3.10-slim

# Variáveis
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instalações de sistema
RUN apt update && apt install -y \
    ffmpeg \
    libsndfile1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY . /app

# Instalar dependências
RUN pip install --upgrade pip \
    && pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu \
    && pip install -r requirements.txt

# Expor porta da aplicação
EXPOSE 8000

# Comando para iniciar o FastAPI com hot reload
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

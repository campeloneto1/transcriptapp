FROM python:3.10-slim

# Instala dependências do sistema
RUN apt update && apt install -y \
    ffmpeg \
    libsndfile1 \
    git \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt

# Instala dependências Python
RUN pip install --upgrade pip \
    && pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir -r requirements.txt \
    && pip show moviepy

# Instala o modelo de linguagem em português do spaCy
RUN python -m spacy download pt_core_news_sm

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

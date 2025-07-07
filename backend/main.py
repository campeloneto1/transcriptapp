
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from backend.transcriber import transcribe_file
from backend.summarizer import summarize_text
import os

app = FastAPI()

@app.post("/upload/", response_class=HTMLResponse)
async def upload(file: UploadFile = File(...)):
    file_path = f"temp_input_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = transcribe_file(file_path)
    summary = summarize_text(text)
    os.remove(file_path)

    return f"""
    <div class="card">
      <div class="label">📝 Transcrição:</div>
      <div>{text}</div>
      <div class="label">📌 Resumo:</div>
      <div>{summary}</div>
    </div>
    """

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("frontend/index.html", encoding="utf-8") as f:
        return f.read()

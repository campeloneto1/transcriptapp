import whisper
import os
import tempfile
import subprocess
from moviepy.editor import VideoFileClip

model = whisper.load_model("base")

def extract_audio(input_path):
    # Se for vídeo, extrai com moviepy
    if input_path.endswith(('.mp4', '.mkv', '.avi', '.mov')):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            clip = VideoFileClip(input_path)
            clip.audio.write_audiofile(temp_audio.name, logger=None)
            return temp_audio.name

    # Se for .ogg, converte com ffmpeg
    if input_path.endswith(".ogg"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            subprocess.run([
                "ffmpeg", "-y", "-i", input_path, temp_audio.name
            ], check=True)
            return temp_audio.name

    # Se já for .mp3, .wav etc., usa direto
    return input_path

def transcribe_file(path):
    try:
        audio_path = extract_audio(path)
        result = model.transcribe(audio_path, language="pt")
        if audio_path != path:
            os.remove(audio_path)
        return result["text"]
    except Exception as e:
        print(f"[ERROR] Falha na transcrição: {e}")
        return f"[ERRO] Não foi possível transcrever o áudio: {e}"

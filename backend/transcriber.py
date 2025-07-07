
import whisper
import os
import tempfile
from moviepy.editor import VideoFileClip

model = whisper.load_model("base")

def extract_audio(input_path):
    if input_path.endswith(('.mp4', '.mkv', '.avi', '.mov')):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            clip = VideoFileClip(input_path)
            clip.audio.write_audiofile(temp_audio.name, logger=None)
            return temp_audio.name
    return input_path

def transcribe_file(path):
    audio_path = extract_audio(path)
    result = model.transcribe(audio_path, language="pt")
    if audio_path != path:
        os.remove(audio_path)
    return result["text"]

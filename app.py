from flask import Flask, request, send_file
from gtts import gTTS
import tempfile
import subprocess
import os

app = Flask(__name__)

@app.route('/generate-video', methods=['POST'])
def generate_video():
    try:
        text = request.json.get('text')
        if not text:
            return {"error": "No text provided"}, 400

        # 텍스트 → 음성 변환 (TTS)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tts_file:
            tts = gTTS(text=text, lang='ko')
            tts.save(tts_file.name)

        # 임시 파일 경로
        video_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4").name

        # FFmpeg 명령어 실행 (subprocess)
        ffmpeg_cmd = [
            'ffmpeg', '-y',
            '-f', 'lavfi', '-i', 'color=c=black:s=1280x720:d=10',
            '-i', tts_file.name,
            '-vf', f"drawtext=text='{text}':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2",
            '-shortest', video_path
        ]

        subprocess.run(ffmpeg_cmd, check=True)

        return send_file(video_path, mimetype='video/mp4')

    except Exception as e:
        return {"error": str(e)}, 500

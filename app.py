from flask import Flask, request, send_file
from gtts import gTTS
import ffmpeg
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '서버가 정상적으로 작동 중입니다! 😊'

@app.route('/generate-video', methods=['POST'])
def generate_video():
    data = request.get_json()
    text = data['text']

    # TTS 음성 생성
    tts = gTTS(text=text, lang='ko')
    tts.save("audio.mp3")

    # 기본 검정 배경 영상 생성
    ffmpeg.input('color=c=black:s=1280x720:d=10', f='lavfi').output(
        'audio.mp3', 'output.mp4', vcodec='libx264', acodec='aac', strict='experimental'
    ).run(overwrite_output=True)

    return send_file('output.mp4', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

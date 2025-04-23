from flask import Flask, request, send_file
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route('/generate-video', methods=['POST'])
def generate_video():
    data = request.get_json()
    summary_text = data.get('text')

    unique_id = str(uuid.uuid4())
    audio_file = f"{unique_id}_output.mp3"
    video_file = f"{unique_id}_output_video.mp4"

    tts = gTTS(text=summary_text, lang='ko')
    tts.save(audio_file)

    ffmpeg_command = f'ffmpeg -y -loop 1 -i background.jpg -i {audio_file} -c:v libx264 -c:a aac -b:a 192k -shortest -pix_fmt yuv420p {video_file}'
    os.system(ffmpeg_command)

    response = send_file(video_file, as_attachment=True)

    os.remove(audio_file)
    os.remove(video_file)

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

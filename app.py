from flask import Flask, request, send_file
import ffmpeg
import os
import uuid

app = Flask(__name__)

@app.route('/generate-video', methods=['POST'])
def generate_video():
    data = request.json
    text = data.get('text', '기본 텍스트')

    # 고유 파일명 생성
    output_file = f"/tmp/{uuid.uuid4()}.mp4"

    # 한글 폰트 경로 (Dockerfile에서 설치 후 사용 가능)
    font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

    (
        ffmpeg
        .input('color=c=black:s=1280x720:d=10', f='lavfi')
        .output(
            output_file,
            vf=f"drawtext=fontfile={font_path}:text='{text}':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2",
            vcodec='libx264',
            pix_fmt='yuv420p',
            t=10
        )
        .run(overwrite_output=True)
    )

    return send_file(output_file, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

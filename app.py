from flask import Flask, request, send_file
import ffmpeg
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '🎬 Video Generator Server Running!'

@app.route('/generate-video', methods=['POST'])
def generate_video():
    data = request.get_json()
    text = data.get('text', '기본 텍스트입니다.')

    # 텍스트 기반 영상 생성 (FFmpeg 사용)
    output_file = 'output.mp4'

    try:
        (
            ffmpeg
            .input('color=c=black:s=1280x720:d=10', f='lavfi')
            .drawtext(
                text=text,
                fontfile='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
                fontsize=48,
                fontcolor='white',
                x='(w-text_w)/2',
                y='(h-text_h)/2',
                box=1,
                boxcolor='black@0.5',
                boxborderw=10
            )
            .output(output_file)
            .run(overwrite_output=True)
        )

        return send_file(output_file, mimetype='video/mp4')

    except Exception as e:
        return {'error': str(e)}, 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

FROM python:3.11

# FFmpeg 설치
RUN apt-get update && apt-get install -y ffmpeg

# 작업 디렉토리 설정
WORKDIR /app

# 현재 디렉토리 모든 파일 복사
COPY . /app

# Python 패키지 설치
RUN pip install -r requirements.txt

# Flask 서버 실행
CMD ["python", "app.py"]

FROM python:3.11-slim

# 필수 패키지 설치
RUN apt-get update && \
    apt-get install -y ffmpeg fonts-nanum && \
    rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY app.py /app/app.py

# 필요한 Python 패키지 설치
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# 서버 실행
CMD ["python", "app.py"]

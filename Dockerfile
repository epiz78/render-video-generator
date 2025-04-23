FROM python:3.11

# 필수 패키지 설치
RUN apt-get update && apt-get install -y ffmpeg

# 작업 디렉토리
WORKDIR /app

# 파일 복사
COPY requirements.txt requirements.txt
COPY app.py app.py

# 패키지 설치
RUN pip install -r requirements.txt

# 포트 노출
EXPOSE 10000

# 실행
CMD ["python", "app.py"]

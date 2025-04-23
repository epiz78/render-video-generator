FROM python:3.11

# FFmpeg 설치
RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 10000
CMD ["python", "app.py"]


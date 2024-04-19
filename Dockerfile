FROM python:3.10-slim

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app

COPY main.py /app/

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Run the Python script
CMD ["python", "main.py"]

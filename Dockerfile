FROM python:3.10.12

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY models/ models/
COPY main.py main.py

CMD ["python", "main.py"]

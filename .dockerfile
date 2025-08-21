FROM python:3.11-slim

# Rust va build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    cargo \
    pkg-config \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

CMD ["gunicorn", "Solar.wsgi:application", "--bind", "0.0.0.0:8000"]

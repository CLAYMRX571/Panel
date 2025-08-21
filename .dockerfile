# Base Python image
FROM python:3.11-slim

# Env sozlamalar
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Rust toolchain uchun tmp
ENV CARGO_HOME=/tmp/cargo
ENV RUSTUP_HOME=/tmp/rustup

# Dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    pkg-config \
    libssl-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Workdir
WORKDIR /app

# Requirements install
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Loyihani copy
COPY . /app/

# Django collectstatic (agar static bo‘lsa)
RUN python manage.py collectstatic --noinput

# Port
EXPOSE 8000

# Runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
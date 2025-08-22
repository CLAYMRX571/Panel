# Python bazaviy image
FROM python:3.11-slim

# System update va kerakli paketlar
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Ishchi papka
WORKDIR /app

# requirements.txt yuklash va o‘rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Loyihani yuklash
COPY . .

# Django uchun port
EXPOSE 8000

# Railway avtomatik PORT beradi
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT"]
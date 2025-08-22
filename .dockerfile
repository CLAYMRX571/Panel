# Python image dan foydalanamiz
FROM python:3.11-slim

# Virtual environment yaratish va ishga tushirish
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip setuptools wheel

# Environment yo‘llarini sozlash
ENV PATH="/opt/venv/bin:$PATH"

# Requirements o‘rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani ko‘chirish
COPY . /app
WORKDIR /app

# Django uchun default port
EXPOSE 8000

# Start komandasi
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
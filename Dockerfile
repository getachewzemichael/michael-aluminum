FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
# Dummy secret key only for collectstatic at build time
ENV SECRET_KEY=build-time-dummy-key-not-used-in-production
ENV DEBUG=False
ENV ALLOWED_HOSTS=*

WORKDIR /app

RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/exists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 10000

CMD python manage.py migrate && gunicorn MichaelAluminum.wsgi:application --bind 0.0.0.0:${PORT:-10000} --workers 2 --timeout 120

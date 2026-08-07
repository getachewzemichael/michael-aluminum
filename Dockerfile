FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV SECRET_KEY=build-time-dummy-key-not-for-production
ENV DEBUG=False
ENV ALLOWED_HOSTS=*

WORKDIR /app

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

COPY docker_start.sh /docker_start.sh
RUN chmod +x /docker_start.sh

EXPOSE 10000

CMD ["/bin/sh", "/docker_start.sh"]

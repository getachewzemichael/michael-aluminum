#!/usr/bin/env bash
# Render build script
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# Create superuser if not exists
python -c "
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MichaelAluminum.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'michaeltadessemiki@gmail.com', 'admin123')
    print('Superuser created.')
else:
    print('Superuser already exists.')
"

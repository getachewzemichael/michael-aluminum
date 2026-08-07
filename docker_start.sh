#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Seeding projects..."
python manage.py seed_projects

echo "Seeding services..."
python manage.py seed_services

echo "Creating superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'michaeltadessemiki@gmail.com', 'admin123')
    print('Superuser created.')
else:
    print('Superuser already exists.')
"

echo "Starting server..."
exec gunicorn MichaelAluminum.wsgi:application --bind 0.0.0.0:${PORT:-10000} --workers 2 --timeout 120

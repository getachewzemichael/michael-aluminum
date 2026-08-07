#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Seeding statistics..."
python manage.py shell -c "
from core.models import StatisticCard
cards = [
    {'value': '30+', 'title': 'Projects Completed', 'description': 'Across Ethiopia',               'icon': 'fa-project-diagram', 'order': 1},
    {'value': '25+', 'title': 'Happy Clients',       'description': 'Satisfied customers nationwide', 'icon': 'fa-smile',           'order': 2},
    {'value': '10+', 'title': 'Years Experience',    'description': 'Expert craftsmanship',           'icon': 'fa-award',           'order': 3},
    {'value': '6',   'title': 'Specialisations',     'description': 'Aluminum, glass and steel',      'icon': 'fa-tools',           'order': 4},
]
for c in cards:
    StatisticCard.objects.update_or_create(title=c['title'], defaults={**c, 'is_active': True})
print('Stats seeded.')
"

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

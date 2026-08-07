#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Seeding Why Choose Us cards..."
python manage.py shell -c "
from core.models import WhyChooseUsCard
cards = [
    {'title': 'Uncompromising Quality', 'description': 'Material quality ወይም workmanship ላይ አንደራደርም — We never cut corners on quality or craftsmanship.', 'icon': 'fa-award', 'order': 1},
    {'title': 'Proven Reliability', 'description': 'በመቶዎች የሚቆጠሩ satisfied clients — Hundreds of clients across Ethiopia have trusted and commended our work.', 'icon': 'fa-handshake', 'order': 2},
    {'title': 'Premium Materials', 'description': 'Top-grade aluminum, tempered glass እና stainless steel — ጥራታቸው ከፍ ያለ materials ብቻ እንጠቀማለን.', 'icon': 'fa-gem', 'order': 3},
    {'title': 'Client-Centered', 'description': 'Every project — client ን ያስደሰተ outcome ለማምጣት tailored approach እንወስዳለን — your satisfaction is our goal.', 'icon': 'fa-users', 'order': 4},
    {'title': 'On-Time Delivery', 'description': 'Deadline ን እናከብራለን — We respect your schedule and deliver every project on time without compromising quality.', 'icon': 'fa-clock', 'order': 5},
    {'title': 'After-Sales Support', 'description': 'Installation ከተጠናቀቀ በኋላም — We provide full after-sales support to ensure lasting satisfaction.', 'icon': 'fa-headset', 'order': 6},
]
for c in cards:
    WhyChooseUsCard.objects.update_or_create(title=c['title'], defaults={**c, 'is_active': True})
print('Why Choose Us seeded.')
"

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
